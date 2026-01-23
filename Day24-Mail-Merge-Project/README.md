# 📬 Mail Merge Project (Python)

A simple yet powerful **Mail Merge application** built using Python.  
This project automates the process of generating personalized invitation letters by replacing placeholders with real names from a file.

---

## 🚀 Project Overview

The Mail Merge Project reads:
- A list of invitee names from a text file
- A template letter containing a placeholder

It then generates **individual personalized letters** for each person and saves them automatically to an output directory.

This project demonstrates practical usage of:
- File handling
- String manipulation
- Automation using Python

---

## 🛠️ Technologies Used

- Python 3
- File Handling (`open`, `read`, `write`)
- String methods (`replace`, `strip`)
- OS-independent relative file paths

---

## 📂 Project Structure
```
Day24-Mail-Merge-Project
│
├── Input
│ ├── Letters
│ │ └── starting_letter.txt
│ │
│ └── Names
│   └── invited_names.txt
│
├── Output
│ │── Ready_To_Send
│ │
  └── main.py

```

---

## 📝 Input Files

### `invited_names.txt`
Contains a list of names, one per line:
```
Jayesh
Piyush
Sidhhant
Kaushal
Raghu
Shubham
Vaishnavi
```

### `starting_letter.txt`
Template letter with a placeholder:
```
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Bhavesh
```
---

## ⚙️ How It Works

1. Reads all names from `invited_names.txt`
2. Reads the template letter from `starting_letter.txt`
3. Replaces the placeholder `[name]` with each actual name
4. Saves personalized letters into the `Output/Ready_To_Send` folder

---

## ▶️ How to Run the Project

1. Clone the repository:
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects/Day24-Mail-Merge-Project.git
```

Navigate to the project directory:

```
cd Day24-Mail-Merge-Project
```
Run the script:
```
python main.py
```
Check the generated letters in:
```
Output/Ready_To_Send/
```
✅ Sample Output
```
letter_for_Jayesh.txt
letter_for_Piyush.txt
letter_for_Sidhhant.txt
...
```
Each file contains a personalized invitation letter.

## 🌱 Possible Enhancements
- Generate .docx files using python-docx

- Add email sending functionality

- Accept dynamic placeholders (e.g., date, venue)

- Add error handling for missing files

## 🎯 Learning Outcomes
- Practical experience with file I/O in Python

- Understanding automation through scripting

- Working with directory structures

- Clean and readable code organization


## 👤 Author

**Bhavesh Vadnere**

Aspiring Software Engineer | Python Developer

🔗 GitHub: https://github.com/BhaveshV23

🔗 LinkedIn: https://www.linkedin.com/in/bhavesh-vadnere

⭐ If you found this project helpful, consider giving it a star!
