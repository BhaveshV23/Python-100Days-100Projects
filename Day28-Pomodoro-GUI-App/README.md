# 🍅 Day 28 – Pomodoro GUI App (Python Tkinter)

A simple and effective **Pomodoro Timer desktop application** built using **Python and Tkinter**.  
This app helps improve focus and productivity using the Pomodoro Technique with visual cues and sound alerts.

---

## 📌 Features

- ⏱️ 25-minute work sessions
- ☕ 5-minute short breaks
- 🧘 20-minute long break after 4 work sessions
- 🔁 Automatic switching between work and break cycles
- 🔔 Sound alert at the end of each session
- ✅ Checkmarks to track completed work sessions
- 🎨 Clean and minimal GUI using Tkinter

---

## 🖥️ Technologies Used

- **Python 3**
- **Tkinter** – for GUI
- **winsound** – for sound alerts (Windows only)

---

## 📸 Preview

> Uses a tomato-themed Pomodoro UI inspired by the classic Pomodoro technique.

<img width="596" height="564" alt="image" src="https://github.com/user-attachments/assets/5408e5cb-fb3e-4c1d-b11a-870ada07a060" />


---

## ⚙️ How It Works

- The timer follows the Pomodoro cycle:
  - 25 min work → 5 min break
  - After 4 work sessions → 20 min long break
- Each completed work session adds a ✔️ checkmark
- A beep sound plays when a session ends
- The Start button is disabled while the timer is running to prevent multiple timers

---

## ▶️ How to Run

1. Clone the repository:
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects/Day28-Pomodoro-GUI-App.git
```

3. Navigate to the project folder:
```
cd Day28-Pomodoro-GUI-App
```

3. Make sure tomato.png is in the same directory.

4. Run the app:
```
python main.py
```

## 📁 Project Structure
```
Day28-Pomodoro-GUI-App/
│
├── main.py
├── tomato.png
└── README.md
```

## 🧠 Key Learning Outcomes

- Tkinter GUI layout using Label, Button, and Canvas

- Using window.after() for countdown timers

- Managing state with global variables

- Formatting time using integer division and modulo

- Preventing multiple event triggers

- Integrating system sound alerts

## 🚀 Future Improvements

- ⏸ Pause / Resume functionality

- 🔕 Sound ON/OFF toggle

- 🌙 Dark mode

- ⚙ Custom work & break durations

- 🧱 Refactor using Object-Oriented Programming (OOP)

## 👤 Author

**Bhavesh Vadnere**

Second-year IT Engineering Student

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://www.linkedin.com/in/bhavesh-vadnere)

⭐ If you like this project, don’t forget to star the repository!
