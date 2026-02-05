# 🃏 Flash Card Language Learning App (Tkinter)

A simple and interactive **flash card application** built using **Python and Tkinter** to help users learn French vocabulary effectively.  
The app displays a French word, flips the card after a short delay to show its English meaning, and tracks learning progress automatically.

---

## 🚀 Features

- 📖 Displays French words with automatic English translation after 3 seconds
- 🔁 Flip-card animation using images
- ✅ Mark words as known to remove them from future practice
- 💾 Progress is saved automatically using CSV files
- 🎉 Completion message when all words are learned
- 🎨 Clean and minimal UI built with Tkinter

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – GUI framework
- **Pandas** – data handling and CSV persistence
- **Random** – random word selection

---

## 📂 Project Structure
```
Day31-Flash-Card-Project/
│
├── data/
│ ├── french_words.csv # Original dataset
│ └── words_to_learn.csv # Auto-generated progress file
│
├── images/
│ ├── card_front.png
│ ├── card_back.png
│ ├── right.png
│ └── wrong.png
│
├── main.py # Application entry point
└── README.md
```

---

## ▶️ How It Works

1. The app loads words from `words_to_learn.csv`
2. If the file doesn’t exist, it falls back to `french_words.csv`
3. A random French word is shown on the flash card
4. After **3 seconds**, the card flips to reveal the English translation
5. Clicking:
   - ❌ **Wrong** → skips to the next word
   - ✅ **Right** → removes the word and saves progress
6. When all words are learned, the app displays a completion message

---

## 🧠 Learning Logic

- Uses `try-except` to handle missing progress files
- Stores words as dictionaries using Pandas
- Automatically saves learning progress after every correct answer
- Prevents timer overlap using `after_cancel()`

---

## 🖥️ How to Run

### Prerequisites
- Python 3.x installed
- Required libraries:
```
  pip install pandas
```
- Run the App
```
python main.py
```
---

## 📈 Possible Improvements

- Add keyboard shortcuts (⬅️ / ➡️)

- Show progress count (e.g., “10 words left”)

- Add support for multiple languages

- Refactor into a class-based architecture

- Add sound effects or animations

## 🎯 Learning Outcomes

- Tkinter GUI development

- File handling and persistence

- Timer-based UI logic

- Real-world project structure

- State management in Python apps

## 👨‍💻 Author

**Bhavesh Vadnere**

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)

⭐ If you like this project, consider giving it a star!
