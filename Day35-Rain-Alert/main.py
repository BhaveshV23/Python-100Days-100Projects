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

MY_LAT=51.507351
MY_LONG=-0.127758

weather_params = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4,
}

try:
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Weather API error: {e}")
    exit()

will_rain = any(hour["weather"][0]["id"] < 700 for hour in weather_data.get("list", []))
if will_rain:
    if all([ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUM, MY_NUM]):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔",
            from_=TWILIO_NUM,
            to=MY_NUM
        )
        print(f"Message Status: {message.status}")
    else:
        print("Error: Missing Twilio credentials in .env file.")
else:
    print("No rain expected in the next 12 hours.")