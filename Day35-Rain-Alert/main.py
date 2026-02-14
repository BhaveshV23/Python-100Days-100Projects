import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("OWM_API_KEY")
MY_LAT=18.520430
MY_LONG=73.856743

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

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
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Rain Alert! ☔\n\nIt's going to rain in the next 12 hours. Grab an umbrella!"
            )
        print("Alert sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
else:
    print("No rain forecast. Enjoy your day!")
