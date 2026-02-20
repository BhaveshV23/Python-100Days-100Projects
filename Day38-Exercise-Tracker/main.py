import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

AUTH_TOKEN= os.getenv("AUTH_TOKEN")

GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 182
AGE = 21

TODAY_DATE = datetime.now().strftime("%d/%m/%Y")
NOW_TIME = datetime.now().strftime("%X")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(f"Nutritionix API call: \n {result} \n")


GOOGLE_SHEET_NAME = "Workout Tracking"
sheet_endpoint= os.getenv("SHEETY_ENDPOINT")


for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME : {
            "date":TODAY_DATE,
            "time":NOW_TIME,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    sheety_headers = {
    "Authorization": f"Bearer {os.getenv('AUTH_TOKEN')}"
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_headers)
    sheet_response.raise_for_status()
    print(f"Sheety Response: \n {sheet_response.text}")