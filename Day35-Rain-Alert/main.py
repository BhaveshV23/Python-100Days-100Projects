import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("OWM_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_NUM = os.getenv("TWILIO_NUMBER")
MY_NUM = os.getenv("MY_VERIFIED_NUMBER")

MY_LAT=18.520430
MY_LONG=73.856743

weather_params = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4,
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

if any(int(hour["weather"][0]["id"]) < 700 for hour in weather_data["list"]):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=TWILIO_NUM,
        to=MY_NUM
    )
    print(message.status)