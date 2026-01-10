# 🐍 Day 20–21: Snake Game (Python)

This project is part of the **100 Days of Code – Python Bootcamp** by **Dr. Angela Yu (Udemy)**.  
The classic **Snake Game** is built using Python’s `turtle` module and follows **Object-Oriented Programming (OOP)** principles.

> 📌 **Note:**  
> Day 20 and Day 21 together form a **single complete project**.  
> - **Day 20:** Core snake movement and controls  
> - **Day 21:** OOP refactoring, food, scoreboard, and collision handling  

---

## 🎮 Game Overview

The player controls a snake that moves around the screen:
- Eat food to grow longer
- Avoid colliding with walls
- Avoid colliding with the snake’s own body

The score increases every time the snake eats food.  
The game ends when a collision occurs.

---

## 🧠 Concepts & Skills Used

- Object-Oriented Programming (OOP)
- Python Classes & Objects
- Inheritance
- Turtle Graphics
- Game Loop & Screen Refreshing
- Collision Detection
- Event Handling (Keyboard Controls)
- Clean Code & Modular Design

---

## 🗂️ Project Structure
```
Day20-21-Snake-Game/
│
├── main.py # Main game loop & screen setup
├── snake.py # Snake class (movement, growth, reset)
├── food.py # Food class (random placement)
├── scoreboard.py # Score tracking & game over display
└── README.md
```


---

## ⌨️ Controls
```
| Key | Action |
|----|--------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |
```
> Reverse direction is automatically prevented.

---

## ▶️ How to Run the Game

### Prerequisites
- Python 3.x installed  
- No external libraries required (uses Python standard library)

### Run
```bash
python main.py
```

## 🧩 Game Logic Summary

• The snake is made of multiple square segments

• Movement is achieved by updating segment positions from tail to head

• Food appears at random locations within the screen bounds

• Score increases when the snake eats food

• Game ends on:

  1. Wall collision

  2. Self-collision (tail)

## 🚀 Improvements Made

• Clean separation of responsibilities using multiple modules

• Constants used instead of magic numbers

• Reset-ready snake structure

• Optimized scoreboard updates

• Readable and maintainable codebase

## 🏆 Learning Outcome

• By completing this project, I strengthened my understanding of:

• Designing real-world Python projects using OOP

• Structuring code across multiple files

• Writing clean, reusable, and scalable logic

• Building interactive games using Turtle graphics

## 📚 Course Reference

100 Days of Code – The Complete Python Pro Bootcamp

Instructor: Dr. Angela Yu

Platform: Udemy

## 👤 Author

**Bhavesh Vadnere**

Information Technology Engineering Student

Aspiring Python Developer | AI & ML Enthusiast
