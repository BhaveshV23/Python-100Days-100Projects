# 🧠 Day 34 – GUI Quiz App (Quizzler)

A desktop-based **Quiz Application** built using **Python**, **Tkinter**, and the **Open Trivia Database API**.  
This project demonstrates **Object-Oriented Programming**, **API integration**, and **GUI-based event handling**.

---

## 🚀 Features

- Fetches real-time quiz questions from an external API
- True / False based quiz format
- Graphical User Interface using Tkinter
- Instant visual feedback (green/red) for answers
- Score tracking throughout the quiz
- Final score display at the end
- Clean separation of logic using OOP principles

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **Requests** (API handling)
- **Open Trivia Database API**
- **Object-Oriented Programming (OOP)**

---

## 📂 Project Structure
```
Day34-GUI-Quiz-App/
│
├── main.py # Application entry point
├── ui.py # GUI logic (Tkinter)
├── quiz_brain.py # Quiz logic and state management
├── question_model.py # Question data model
├── data.py # API request and data handling
├── images/
│ ├── true.png
│ └── false.png
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects.git
```

### 2️⃣ Navigate to the project folder
```
cd Python-100Days-100Projects/Day34-GUI-Quiz-App
```

### 3️⃣ Install dependencies
```
pip install requests
```

### 4️⃣ Run the application
```
python main.py
```

## 🧠 How It Works

- The app fetches quiz questions from the Open Trivia Database API.

- Each question is converted into a Question object.

- QuizBrain manages:

  - Current question

  - Score

  - Answer validation

- QuizInterface handles:

  - UI rendering

  - Button events

  - Visual feedback

- Buttons are temporarily disabled after each answer to prevent double-click issues.

- The final score is shown once all questions are answered.

## 🧪 Sample API Configuration
```
parameters = {
    "amount": 10,
    "type": "boolean"
}
```

You can customize:

- Number of questions

- Difficulty

- Category

## 📸 UI Feedback Logic

✅ Correct Answer → Green background

❌ Wrong Answer → Red background

⏱ Feedback visible for 1 second before moving to next question

## 📈 Possible Improvements

- Add difficulty and category selection

- Add progress bar or timer

- Restart quiz option

- Keyboard shortcuts for answers

- Unit testing for quiz logic

- Dark / Light theme toggle

## 🎯 Learning Outcomes

- GUI development with Tkinter

- API data handling in Python

- Event-driven programming

- State management in GUI apps

- Clean project architecture using OOP

## 👤 Author

**Bhavesh Vadnere**

📌 Information Technology Engineering Student

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)

⭐ If you found this project useful, feel free to star the repository!
