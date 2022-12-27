from db import selectAllWorkouts, deleteOneWorkout, insertOneWorkout
import streamlit as st
from datetime import datetime
from ytExtractor import search
import random
@st.cache(allow_output_mutation=True)
def getAllWorkouts():
    return selectAllWorkouts()

st.title("Workout Web App")

st.markdown("""
    This web app allows you to manage your **daily workouts** for you to hit your goal easily! 
""")

t = st.sidebar.empty()

menu_options = ("Today's workout", "All workouts", "Add workout")
selection = st.sidebar.selectbox("Pages", menu_options)

if selection=="Today's workout":
    st.markdown("Today's workout'")
    workouts= selectAllWorkouts()

    if not workouts:
        st.write("There is no workout in database!")

    else:
        n=len(workouts)
        workout = workouts[0,n-1]

        if st.button("Choose another workout"):
            workouts = selectAllWorkouts()
            workout_new = workouts[0,n-1]

            while workout_new["workoutId"] == workout["workoutId"]:
                workout_new = workouts[0,n-1]
            
            workout = workout_new

        st.text(workout["workoutName"])
        st.video(workout["videoLink"])


elif selection == "All workouts":
    st.markdown('<p style="font-family: Brush Script MT,cursive; color:black; font-size: 42px;">All Workouts</p>',unsafe_allow_html=True)
    
    workouts = getAllWorkouts()
    for workout in workouts:
        url = workout["video_link"]
        st.text(workout['workoutName'])
        # st.text(f"{workout['channel']} - {get_duration_text(workout['duration'])}")
        
        ok = st.button('Delete workout', key=workout["workoutId"])
        if ok:
            deleteOneWorkout(workout["workoutId"])
            st.legacy_caching.clear_cache()
            st.experimental_rerun()
            
        st.video(url)
    else:
        st.text("No workouts in Database!")
else:
    #  add workout
    st.markdown("## Add workout")

    url = st.text_input("Enter the URL")

    if url:
        workout_data = search(url)

        if workout_data:
            st.text("Title:",search["title"])
            st.text("Channel:",search["channel"])
            # displays a video player   
            st.video(url)
            if(st.button("Add workout")):
                insertOneWorkout(search["id"],search["title"],url)
                st.text("Workout has been added successfully!")
                # clear cache
                st.legacy_caching.clear_cache()
        else:
            st.text("No workout is found!")

    else:
        st.text("No workout is found!")
while True:
    # t.markdown(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t.header(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))