import requests
import json

url = "https://gymweb-quintonpyx.harperdbcloud.com"
authorization = "Basic YWRtaW46MTIzNDU2"
headers =  {
    'Content-Type': 'application/json',
    'Authorization': authorization
  }
def createSchema(schema):
  payload = json.dumps({
    "operation": "create_schema",
    "schema": schema
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
  

def createTable(schema, table, hash_attribute):
  payload = json.dumps({
    "operation": "create_table",
    "schema": schema,
    "table": table,
    "hash_attribute": hash_attribute
})

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

def insertOneWorkout(workoutId,workoutName, videoLink):
  payload = json.dumps({
    "operation": "insert",
    "schema": "workoutweb",
    "table": "workout",
    "records": [
        {
            "workoutId": workoutId,
            "workoutName": workoutName,
            "videoLink": videoLink,
        }
    ]
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
  

def deleteOneWorkout(workoutId):
  payload = json.dumps({
    "operation": "delete",
    "table": "workoutweb",
    "schema": "workout",
    "hash_values": [
        workoutId
    ]
})

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

def updateOneWorkout(workoutId,newWorkoutName):
  payload = json.dumps({
    "operation": "update",
    "schema": "workoutweb",
    "table": "workout",
    "records": [
        {
            "workoutId": workoutId,
            "workoutName": newWorkoutName
        }
    ]
})

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

def selectAllWorkouts():
  payload = json.dumps({
    "operation": "sql",
    "sql": "SELECT * FROM workoutweb.workout"
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
  
def addToSchedule(scheduleId,date):
  payload = json.dumps({
    "operation": "insert",
    "schema": "workoutweb",
    "table": "schedule",
    "records": [
        {
            "scheduleId": scheduleId,
            "date": date,
        }
    ]
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

createSchema("workoutweb")
createTable("workoutweb","workout","workoutId")
createTable("workoutweb","schedule","scheduleId")
