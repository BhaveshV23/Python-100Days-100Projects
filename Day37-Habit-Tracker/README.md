# Day 37 – Habit Tracker (Pixela API)

A command-line **Habit Tracker** built using Python and the **Pixela REST API**.  
This project allows users to **track daily cycling distance** by creating, updating, and deleting habit records (pixels) on a Pixela graph.

---

## 📌 Features

- 📊 Create a habit graph on Pixela
- ➕ Add daily habit data (kilometers cycled)
- ✏️ Update existing habit entries
- ❌ Delete habit entries with confirmation
- 🔐 Secure authentication using environment variables
- 🧠 Input validation to prevent invalid data

---

## 🛠️ Tech Stack

- **Python 3**
- **Requests** – HTTP requests
- **Pixela API** – Habit tracking backend
- **python-dotenv** – Environment variable management

---

## 📂 Project Structure

```
Day37-Habit-Tracker/
│
├── main.py
├── .env
├── README.md
└── .gitignore
```
---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects.git
cd Python-100Days-100Projects/Day37-Habit-Tracker
```

### 2. Install Dependencies
```
pip install requests python-dotenv
```

### 3. Configure Environment Variables

Create a .env file in the project directory:
```
MY_USERNAME=your_pixela_username
TOKEN=your_pixela_token
GRAPH_ID=cycling1
```
⚠️ Never commit .env files to GitHub

### 4. Run the program:
```
python main.py
```

### You’ll be prompted to choose an action:

```What would you like to do? (add/update/delete):```

➕ Add Pixel

Logs today’s cycling distance.

✏️ Update Pixel

Corrects today’s existing entry.

❌ Delete Pixel

Deletes today’s entry after confirmation.

---

## 🔐 API Workflow

This project follows proper REST principles:

| Action       | HTTP Method |
| ------------ | ----------- |
| Create pixel | POST        |
| Update pixel | PUT         |
| Delete pixel | DELETE      |

Authentication is handled using request headers: X-USER-TOKEN

---

## 🧠 What I Learned

- Working with REST APIs

- Using correct HTTP methods

- Handling authentication securely

- Structuring Python scripts professionally

- Input validation and error handling

- CLI-based user interaction

---

## 📈 Future Improvements

- Add support for multiple habits

- CLI arguments using argparse

- Automated daily logging (cron / task scheduler)

- Data visualization export

- Retry & logging mechanisms

---

## 🧑‍💻 Author

**Bhavesh Vadnere**

Python Developer

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)
