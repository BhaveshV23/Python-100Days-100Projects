# 🚀 Day 33 – ISS Overhead Notifier

An automated Python script that sends you an email when the International Space Station (ISS) is passing overhead at your location during nighttime.

This project uses public APIs to track the ISS position and determine local sunrise/sunset time.

## 🌍 How It Works

The program runs continuously and checks every 60 seconds:

1. 📡 Fetches the current ISS location using the Open Notify API

2. 🌅 Checks whether it is currently nighttime using the Sunrise-Sunset API

3. 📧 Sends you an email notification if:

  - The ISS is within ±5° latitude and longitude of your location

  - It is currently dark at your location

## 🔌 APIs Used

- 🛰️ ISS Location API
```
http://api.open-notify.org/iss-now.json
```

- 🌞 Sunrise & Sunset API
```
https://api.sunrise-sunset.org/json
```

## 🛠️ Technologies Used

- Python 3

- requests

- datetime

- smtplib

- time

- python-dotenv

- Gmail SMTP

## 📂 Project Structure
```
Day33-ISS-Overhead-Notifier-Project/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects.git
cd Python-100Days-100Projects/Day33-ISS-Overhead-Notifier-Project
```

### 2️⃣ Install Dependencies
```
pip install requests python-dotenv
```

### 3️⃣ Create a .env File

Create a .env file in the root directory:

MY_EMAIL=your_email@gmail.com

MY_PASSWORD=your_app_password

#### ⚠️ Important:

Use a Google App Password, NOT your real Gmail password.

### 4️⃣ Set Your Location

Modify these variables in main.py:

MY_LAT = 18.520430

MY_LONG = 73.856743

Replace with your own latitude and longitude.

### 5️⃣ Run the Program
```
python main.py
```

## 🧠 Key Concepts Practiced

- Working with REST APIs

- Handling JSON data

- Environment variables for security

- SMTP email automation

- Exception handling with raise_for_status()

- Infinite loops with timed intervals

- Timezone-aware datetime handling

## 🔐 Security Best Practice

- Sensitive data is stored in .env

- .env is added to .gitignore

- Prevents exposing credentials on GitHub

## 🚀 Future Improvements

- Send SMS instead of email

- Deploy on a cloud server (AWS / Railway / Render)

- Add logging

- Convert into a desktop notification app

- Add multiple recipient support

## 👨‍💻 Author

**Bhavesh Vadnere**

Engineering Student | Python Developer | AI Enthusiast

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)
