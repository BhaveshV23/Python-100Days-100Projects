# NATO Phonetic Alphabet Converter 🔤

## 📌 Project Overview
This project is a Python program that converts user-entered words or names into their corresponding **NATO phonetic alphabet** representation.

Unlike a basic implementation, this version includes **robust input validation**:
- ✅ Allows spaces (e.g., full names)
- ❌ Rejects numbers and special characters
- ❌ Prevents empty or misleading output
- ✔ Provides clear user feedback

The project is part of the **100 Days of Code – Python Bootcamp (Day 26)**.

---

## 🛠️ Technologies Used
- **Python 3**
- **Pandas**
- **CSV File Handling**

---

## 📂 Project Structure
```
Day26-NATO-Alphabet/
│
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

---

## 📄 How It Works
1. The program reads `nato_phonetic_alphabet.csv` using pandas.
2. A dictionary is created that maps each alphabet letter (A–Z) to its NATO code word.
3. The user is prompted to enter a word or name.
4. Spaces are allowed, but digits and special characters are rejected.
5. Each valid letter is converted to its NATO phonetic equivalent.
6. The final phonetic output is displayed as a list.

---

## 🔍 Input Validation Logic
To ensure correct and predictable behavior, the program uses the following logic:

- Spaces are **allowed** so users can enter full names.
- Input is validated **after removing spaces**.
- If the cleaned input contains anything other than letters A–Z, the program rejects it.

### Example Validation Code
```
cleaned_word = word.replace(" ", "")

if not cleaned_word.isalpha():
    print("Invalid input. Use letters A–Z only (spaces are allowed).")
```

This prevents issues such as:

- Silent ignoring of digits

- Empty output lists ([])

- Unexpected crashes

## ▶️ Example Usage

✅ Valid Input
```
Enter a word: Bhavesh Vadnere
```

Output
```
['Bravo', 'Hotel', 'Alfa', 'Victor', 'Echo', 'Sierra', 'Hotel',
 'Victor', 'Alfa', 'Delta', 'November', 'Echo', 'Romeo', 'Echo']
```

## 🧠 Key Concepts Practiced

- Dictionary comprehension

- List comprehension

- Reading CSV files using pandas

- Input normalization

- Input validation

- Clean control flow (without misusing try/except)


## 📌 Possible Enhancements

- Convert logic into reusable functions

- Display phonetic output word-by-word

- Add audio pronunciation

- Build a GUI using Tkinter

## 👤 Author

**Bhavesh Vadnere**

Aspiring Python Developer | AI & ML Enthusiast

GitHub: https://github.com/BhaveshV23 

LinkedIn: https://www.linkedin.com/in/bhavesh-vadnere

⭐ If you like this project, consider giving it a star on GitHub!
