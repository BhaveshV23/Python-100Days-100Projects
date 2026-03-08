# 🛒 Day 47 – Amazon Live Price Tracker

A Python automation project that tracks the price of an Amazon product and sends an email alert when the price drops below a specified value.

This project demonstrates **web scraping, environment variable management, and email automation using Python**.

---

## 📌 Features

* Scrapes product data directly from Amazon
* Extracts **product title and price**
* Compares the price with a predefined **target price**
* Sends an **email notification** when the price drops
* Uses **environment variables (.env)** to securely store credentials

---

## 🧠 Concepts Used

* Python Web Scraping
* `requests` library
* `BeautifulSoup`
* Environment Variables with `python-dotenv`
* Email automation using `smtplib`
* HTTP headers to mimic browser requests

---

## 🛠️ Technologies Used

* Python 3
* BeautifulSoup4
* Requests
* SMTP (Email automation)
* python-dotenv

---

## 📂 Project Structure

```
Day47-Live-Price-Tracker
│
├── main.py
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/BhaveshV23/Python-100Days-100Projects.git
```

Navigate to the project folder:

```bash
cd Day47-Live-Price-Tracker
```

---

## 🔑 Environment Variables

Create a `.env` file and add the following variables:

```
SMTP_ADDRESS=smtp.gmail.com
SENDER_EMAIL=your_email@gmail.com
PASSWORD=your_app_password
RECEIVER_EMAIL=receiver_email@gmail.com
```

⚠️ If you are using Gmail, you must generate an **App Password**.

---

## 🚀 How It Works

1. The script sends an HTTP request to the Amazon product page.
2. `BeautifulSoup` parses the HTML content.
3. The program extracts:

   * Product title
   * Current price
4. If the current price is **lower than the target price**, an email notification is sent.

---

## 📧 Example Email Alert

```
Subject: Amazon Price Alert!

Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is on sale for 7338.68!
https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1
```

---

## ▶️ Run the Script

```bash
python main.py
```

---

## ⚠️ Note

Amazon frequently updates its HTML structure, which may break web scraping scripts.
If the script stops working, the HTML selectors may need to be updated.

---

## 📈 Future Improvements

* Track price history in a database
* Send notifications via Telegram or WhatsApp
* Monitor multiple products simultaneously
* Schedule automatic checks using **cron jobs or Task Scheduler**

---

## 👨‍💻 Author

**Bhavesh Vadnere**

* GitHub: [BhaveshV23](https://github.com/BhaveshV23)
* YouTube: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)
