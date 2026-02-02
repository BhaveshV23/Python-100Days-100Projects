# 🔐 Password Manager (Tkinter)

A simple **Password Manager desktop application** built using **Python and Tkinter**.  
This app allows users to **generate strong passwords**, **store credentials securely in a JSON file**, and **retrieve saved login details** easily.

This project is part of my **100 Days of Code – Python Bootcamp** journey.

---

## 🚀 Features

- 🔑 Generate strong random passwords
- 📋 Automatically copy generated password to clipboard
- 💾 Save website, email/username, and password locally
- 🔍 Search and retrieve saved credentials by website name
- ⚠️ Input validation with user-friendly error messages
- 📁 Persistent storage using `data.json`
- 🖥️ Clean and simple Tkinter GUI

---

## 🛠️ Tech Stack

- **Python**
- **Tkinter** (GUI)
- **JSON** (Data storage)
- **pyperclip** (Clipboard support)
- **random & string** (Password generation)

---

## 📸 Application Preview

<img width="638" height="542" alt="screen-image" src="https://github.com/user-attachments/assets/8f4646ec-00d7-40cb-9c31-90f15a257629" />

---

## 📂 Project Structure
```
Password-Manager/
│
├── main.py # Main application logic
├── data.json # Stores saved credentials
├── logo.png # App logo
└── README.md # Project documentation
```


---

## 🔑 Password Generation Logic

- Uses:
  - Uppercase & lowercase letters
  - Numbers
  - Special characters
- Randomized length and shuffled characters
- Automatically copies password to clipboard for convenience

---

## 💾 Data Storage Format

Credentials are stored in a structured JSON format:

```
{
  "google": {
    "email": "example@gmail.com",
    "password": "P@ssw0rd!"
  }
}
```

Website names are normalized (lowercase & stripped) to avoid duplicates caused by case differences.

---

## 🔍 How Search Works

- User enters a website name

- App checks data.json

- If found → displays email & password

- If not found → shows an appropriate error message

---

## ⚠️ Known Limitations

- Passwords are currently stored in plain text

- Duplicate website entries overwrite existing data

- No master password or authentication layer

- Local storage only (no cloud sync)

---

## 🚧 Future Improvements

These enhancements are planned to make the project more secure and scalable:

### 🔁 Handle Duplicate Entries

- Detect if a website already exists

- Prompt user to:

  - Overwrite existing credentials OR

  - Cancel saving to prevent accidental data loss

### 🔐 Encrypt Stored Passwords

- Encrypt passwords before saving them to data.json

- Possible approaches:

  - cryptography (Fernet encryption)

  - Hashing with salt for improved security

- Decrypt only when displaying to the user

### 👁️ Show / Hide Password Toggle

- Improve usability by allowing users to toggle password visibility

### 🗂️ Multiple Accounts per Website

- Support storing more than one account (personal/work) per website

### 🎨 UI Enhancements

- Dark mode

- Better spacing and styling

- Keyboard shortcuts

---

## 🧠 What I Learned

- Building GUI applications using Tkinter

- File handling with JSON

- Error handling using try-except

- Improving user experience with validations

- Structuring real-world Python projects

---

## Author

**Bhavesh Vadnere**

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)

⭐ If you like this project, feel free to star the repository!
