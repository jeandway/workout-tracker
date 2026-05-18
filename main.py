import requests
from datetime import datetime
GENDER = "female"
WEIGHT_KG = 57
HEIGHT_CM = 161
AGE = 33

APP_ID = 'your_app_id'
API_KEY = 'your_api_key'

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query" : exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
}

sheety_endpoint = "https://api.sheety.co/4fe386f87112bf77ccf09cc3ce22b6a4/myWorkouts/workouts"
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

response = requests.post(
    url=exercise_endpoint,
    json=parameters,
    headers=headers
)

result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
    )
    print(sheet_response.text)