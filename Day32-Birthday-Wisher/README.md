## 🎂 Day 32 – Birthday Wisher (Email Automation)

An automated birthday email sender built using Python.
This script checks today's date, matches it with birthdays stored in a CSV file, and automatically sends a personalized birthday email.

This project is part of my 100 Days of Code – Python Pro Bootcamp journey.

## 🚀 Features

-  Automatically checks today's date

-  Reads birthday data from a CSV file

-  Selects a random birthday letter template

-  Sends personalized birthday emails via SMTP

-  Uses environment variables for secure credentials handling

## 🛠️ Technologies Used

- Python 3

- pandas

- smtplib

- datetime

## 📁 Project Structure
```
Day32-Birthday-Wisher/
│
├── main.py
├── birthdays.csv
├── .env
|── .gitignore
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── README.md
```

## 🔐 Environment Variables Setup

Create a .env file in your project root:

```MY_EMAIL=your_email@gmail.com```

```MY_PASSWORD=your_app_password```

⚠️ Important (For Gmail Users)

- Enable 2-Step Verification

- Generate an App Password

- Use the App Password instead of your real Gmail password

## ▶️ How to Run

Clone the repository:
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects.git
```

Navigate into the project folder:
```
cd Python-100Days-100Projects/Day32-Birthday-Wisher
```

Install dependencies:
```
pip install pandas python-dotenv
```

Run the script:
```
python main.py
```

## 🧠 How It Works

- Gets today’s month and day.

- Reads birthday data using pandas.

- Filters rows matching today's date.

- Selects a random letter template.

- Replaces [NAME] placeholder.

- Sends email using SMTP with TLS security.

## 🔮 Future Improvements

- Add logging system

- Add error handling for failed emails

- Deploy on a cloud server (AWS / Render)

- Schedule daily run using:

- Windows Task Scheduler

- Cron Job (Linux/Mac)

## 📚 Learning Outcome

- Through this project, I learned:

- Working with CSV files using pandas

- Sending emails using smtplib

- Using environment variables securely

- Automating real-world workflows with Python

## 📌 Author

**Bhavesh Vadnere**

Second Year IT Engineering Student

Learning Python, AI & Full Stack Development

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)
