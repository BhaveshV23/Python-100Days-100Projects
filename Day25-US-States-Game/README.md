# 🗺️ U.S. States Guessing Game (Python)

An interactive Python game that helps users learn and test their knowledge of U.S. state names.  
Correctly guessed states are displayed at their geographical locations on a U.S. map using Turtle graphics.

This project is part of **Day 25** of the *100 Days of Code – Python Bootcamp*.

---

## 📌 Project Overview

The U.S. States Game prompts users to guess the names of all 50 U.S. states.  
Each correct guess is written directly onto a blank U.S. map at the appropriate coordinates.  
If the user exits before completing all guesses, the program generates a CSV file listing the states they missed.

---

## 🎮 How the Game Works

1. A blank U.S. map is displayed using Turtle graphics.
2. The user is prompted to enter a U.S. state name.
3. If the guess is correct:
   - The state name is written on the map at the correct location.
   - The score updates automatically.
4. The game continues until:
   - All 50 states are guessed, **or**
   - The user types **`Exit`**.
5. Upon exit, a `states_to_learn.csv` file is generated containing all unguessed states.

---

## 🧠 Key Concepts Used

- Turtle Graphics for visualization
- Pandas for CSV data handling
- Sets for efficient data storage
- Loops and conditional logic
- User input handling and validation
- File generation using Pandas DataFrame

---

## 📂 Project Structure
```
Day25-US-States-Game/
│
├── main.py # Main game logic
├── 50_states.csv # State names with x,y coordinates
├── blank_states_img.gif # Blank U.S. map image
├── states_to_learn.csv # Generated after exiting the game
└── README.md
```


---

## ▶️ How to Run the Project

### 1️⃣ Install Requirements
Make sure Python is installed, then install pandas:
```
pip install pandas
```

### 2️⃣ Run the Game
```
python main.py
```

## 📈 Improvements Over Basic Version

- Uses a set to prevent duplicate guesses

- Handles user cancel input safely

- Uses a single Turtle instance for efficient drawing

- Automatically generates a learning CSV on exit

- Cleaner and more robust game logic

## 🚀 Possible Enhancements

- Add a timer or challenge mode

- Show feedback for incorrect guesses

- Highlight missed states visually

- Convert the game into a GUI application

- Add sound effects or animations

## 📚 Learning Outcomes

- Through this project, I practiced:

- Reading and filtering real-world datasets

- Visualizing data using Turtle graphics

- Writing clean, robust Python code

- Handling user input edge cases

- Structuring a small but complete Python application

## 🧑‍💻 Author

**Bhavesh Vadnere**

Engineering Student | Python & SQL Learner

GitHub: https://github.com/BhaveshV23

LinkedIn: https://www.linkedin.com/in/bhavesh-vadnere


⭐ If you like this project, consider starring the repository!
