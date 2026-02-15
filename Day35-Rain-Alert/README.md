# 🌧️ Rain Alert Notification System (Day 35)

A Python automation script that checks the weather forecast using the OpenWeather API and sends an SMS alert via Twilio if rain is expected in the next few hours.

This project is part of my **100 Days of Code – Python** journey.

---

## 🚀 Features

- Fetches real-time weather forecast data
- Detects rain using OpenWeather weather condition codes
- Sends SMS alerts using Twilio
- Secure credential management with environment variables
- Graceful error handling for network and configuration issues

---

## 🛠️ Technologies Used

- Python 3
- Requests (HTTP API calls)
- OpenWeather API
- Twilio API
- python-dotenv

---

## 📁 Folder Structure
```
Day35-Rain-Alert/
   ├── main.py
   ├── README.md
   └── .gitignore
```

---

## 📍 How It Works

1. Fetches the next **4 forecast intervals (~12 hours)** from OpenWeather.
2. Checks weather condition codes:
   - Codes `< 700` indicate rain, snow, or drizzle.
3. If rain is detected:
   - Sends an SMS alert to the verified phone number using Twilio.
4. If no rain is expected:
   - Prints a friendly message to the console.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects.git
cd Python-100Days-100Projects/Day35-Rain-Alert
```

### 2️⃣ Install Dependencies
```
pip install requests python-dotenv twilio
```

### 3️⃣ Configure Environment Variables

Create a .env file in the project directory:
```
OWM_API_KEY=your_openweather_api_key
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=your_twilio_phone_number
MY_VERIFIED_NUMBER=your_verified_phone_number
```

### 4️⃣ Run the Script
```
python main.py
```

🌍 Location Configuration

You can change the location by modifying latitude and longitude values:
```
MY_LAT = 51.507351
MY_LONG = -0.127758
```

---

## 📌 Example Output

If rain is expected:

`Message Status: queued`


If no rain is expected:

`No rain expected in the next 12 hours.`

---

## 🧠 Key Learnings

- Working with third-party APIs

- Using environment variables securely

- Defensive programming with error handling

- Writing clean, Pythonic code using any()

---

## Author

**Bhavesh Vadnere**

Engineering student | Python Developer

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

Linkedin: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)
