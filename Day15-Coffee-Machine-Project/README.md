# ☕ Day 15 – Coffee Machine Project (Python)

This project is part of the **100 Days of Code – Python Pro Bootcamp** by **Dr. Angela Yu**.  
It simulates a **console-based coffee machine** that manages resources, processes coin payments, and serves drinks like a real coffee machine.

---

## 📌 Project Overview

The Coffee Machine program allows users to:
- Choose a drink (espresso, latte, cappuccino)
- Insert coins for payment
- Check available resources
- Receive change if extra money is inserted
- Turn off the machine or view a report

The project focuses on **functions, dictionaries, loops, and conditional logic** in Python.

---

## 🛠️ Features

- ☕ Drink options: **Espresso, Latte, Cappuccino**
- 💰 Coin-based payment system
- 📊 Resource and profit reporting
- ❌ Handles insufficient resources or money
- 🔁 Continuous operation until turned off

---

## 🧠 Concepts Used

- Python dictionaries
- Functions & return values
- Loops (`while`)
- Conditional statements
- Global variables
- User input handling

---

## 📋 Menu Configuration

```python
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}
```

## ▶️ How to Run the Project

Make sure Python 3 is installed

Clone the repository:
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects.git
```

Navigate to the project folder

Run the script:
```
python coffee_machine.py
```

## ⌨️ User Commands
```
| Command                       | Description                        |
| ----------------------------- | ---------------------------------- |
| espresso / latte / cappuccino | Order a drink                      |
| report                        | View available resources and money |
| off                           | Turn off the coffee machine        |
```

## 🧪 Example Output
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 12
how many dimes?: 12
how many nickles?: 12
how many pennies?: 12
Here is $2.42 in change.
Here is your latte ☕️. Enjoy!
What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
What would you like? (espresso/latte/cappuccino): off
```

## 🎯 Learning Outcome

• By completing this project, I learned:

• How to structure a program using multiple functions

• Managing shared state with global variables

• Simulating real-world systems using Python logic

• Writing cleaner, modular, and readable code

## 🚀 Next Steps

• Add OOP version of the coffee machine

• Store resources persistently using files

• Create a GUI version using Tkinter

## Author
**Bhavesh Vadnere**

IT Enthusiast 
