# 🪢 Day 07 – Hangman Game

A project from the course **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

---

## 📌 Overview

The **Hangman Game** is a classic word-guessing game where the player must uncover a hidden word by guessing letters. Each wrong guess reduces the player's lives, and when all lives are gone... the hangman appears!

This project reinforces concepts like loops, conditionals, lists, string manipulation, and module imports.

---

## 📚 Topics Practiced

* Importing external Python files
* Random module (`random.choice`)
* Loops and conditionals
* String operations
* ASCII art rendering
* Game logic construction
* Handling user input

---

## 🗂️ Project Structure
```
Day07-Hangman-Game/
│── main.py
│── hangman_words.py
│── hangman_art.py
└── README.md
```
---

## ▶️ How to Run

### 1. Clone the main repository:

```bash
git clone [https://github.com/BhaveshV23/Python-100Days-100Projects.git](https://github.com/BhaveshV23/Python-100Days-100Projects.git)
```

### 2. Navigate to this project:
```
cd Python-100Days-100Projects/Day07-Hangman-Game
```

### 3. Run the game:
```
python main.py
```
## 🎮 Game Rules

• You start with 6 lives.

• A word is chosen randomly from word_list.

• Guess letters one by one.

• Wrong guesses reduce lives.

• Already guessed letters are detected.

• The game ends when:

  You guess all letters → YOU WIN 🎉

  Lives reach 0 → YOU LOSE 💀 (The word is revealed)


## 🧩 Key Features
✔ Word chosen randomly

✔ Tracks correct letters guessed

✔ Detects duplicates

✔ ASCII hangman stages displayed

✔ Life counter shown each round

✔ Win/Lose endings with clear messages

## 🖥️ Sample Output
```
 _                                       
| |                                      
| |__  __ _ _ __  __ _ _ __ ___  __ _ _ __ 
| '_ \/ _` | '_ \/ _` | '_ ` _ \/ _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                  __/ |                      
                 |___/                       

Word to guess: _ _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: a _ a _ _
```

## 🧠 Code Logic Summary
• A random word is selected using: Python
chosen_word = random.choice(word_list)

• Lives start at 6 and decrease on incorrect guesses.

• Correct guesses update the display.

• ASCII art is shown using: Python
print(stages[lives])

• Game ends when: Python
"_" not in display  # Win
lives == 0          # Lose


## 💻 Source Code (main.py)
Python
```
import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

```

## 🚀 Future Improvements
• Add difficulty levels

• Add GUI version (Tkinter)

• Add replay option

• Add scoring system

• Hide the answer to avoid spoilers 😄

## ⭐ Acknowledgment
This project is part of my journey through the 100 Days of Code – The Complete Python Pro Bootcamp by Dr. Angela Yu and belongs to my repo: Python-100Days-100Projects.
