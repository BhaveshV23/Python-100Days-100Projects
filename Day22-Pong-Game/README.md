# 🏓 Day 22 – Pong Game (Python Turtle)

A classic **Pong Game** built using Python’s `turtle` graphics module as part of  **Day 22** of the **100 Days of Code – Python Bootcamp** by **Dr. Angela Yu**.

This project demonstrates **Object-Oriented Programming (OOP)**, collision detection, game loops, and basic game physics.

---

## 🎯 Project Objectives

- Understand OOP concepts through a game-based project
- Implement real-time movement and collision detection
- Work with multiple Python modules
- Build a playable 2D game using the Turtle library

---

## 🕹️ Gameplay Overview

- Two paddles (Left & Right) controlled by players
- A ball that bounces off paddles and walls
- Score increases when the opponent misses the ball
- Game ends when a player reaches the winning score

---

## 🎮 Controls

| Player | Action        | Key |
|------|---------------|-----|
| Left Paddle | Move Up   | `W` |
| Left Paddle | Move Down | `S` |
| Right Paddle | Move Up | `↑` |
| Right Paddle | Move Down | `↓` |

---

## 🧱 Project Structure

```text
Day22-Pong-Game/
│
├── main.py          # Main game loop and event handling
├── paddle.py        # Paddle class with movement and boundary checks
├── ball.py          # Ball class with physics and speed control
├── scoreboard.py    # Scoreboard and game-over logic
└── README.md        # Project documentation
```

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)

- Python Turtle Graphics

- Game loop & animation (tracer, update)

- Collision detection

- Keyboard event handling

- Incremental difficulty

- Defensive programming (edge cases)

## ⚙️ Features

- Smooth paddle movement
- Ball speed increases after paddle hits
- Angle-based ball reflection
- Paddle boundary restrictions
- Score tracking
- Game-over condition

## 🚀 How to Run the Project

- Make sure Python is installed (Python 3.8+ recommended)

- Clone this repository or download the files

- Navigate to the project folder

- Run the game:
```
python main.py
```

## 🧪 Edge Cases Handled

- Prevent paddles from moving off-screen

- Avoid multiple ball bounces in a single frame

- Reset ball speed and direction after scoring

- Accurate paddle collision detection at high speed

## 🛠️ Possible Enhancements

- AI-controlled paddle

- Sound effects

- Pause / Resume functionality

- Difficulty levels

- Power-ups

- Conversion to pygame

## 📚 Learning Outcome

This project strengthened my understanding of:

- Game physics fundamentals

- Modular code design

- Real-time input handling

- Writing scalable and readable Python code

## 👨‍💻 Author

**Bhavesh Vadnere**

🎓 IT Engineering Student | Python
