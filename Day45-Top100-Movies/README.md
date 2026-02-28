# 🎬 Day 45 – Top 100 Movies Web Scraper

The script scrapes **Empire Online’s Top 100 Movies of All Time** list using **BeautifulSoup** and saves the movie titles into a text file in the correct order.

---

## 📌 Project Overview

- Scrapes movie titles from a archived Empire Online webpage
- Extracts the **Top 100 Movies**
- Reverses the list to maintain ranking order (1 → 100)
- Saves results into a `movies.txt` file

---

## 🛠️ Technologies Used

- Python 🐍
- `requests`
- `beautifulsoup4`
- File handling
- Web scraping fundamentals

---

## 📂 Project Structure
```
Day45-Top100-Movies/
│
├── main.py
├── movies.txt
└── README.md
```


---

## ⚙️ How It Works

1. Sends a GET request to the archived Empire Online webpage  
2. Parses HTML using BeautifulSoup  
3. Extracts movie titles from `<h3 class="title">` tags  
4. Reverses the list to correct ranking order  
5. Writes the movie titles into `movies.txt`

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```
pip install requests beautifulsoup4
```

### 2️⃣ Run the Script
```
python main.py
```

---

## 📄 Output Example (movies.txt)
<img width="538" height="239" alt="output-image" src="https://github.com/user-attachments/assets/35ff0750-a9f9-499f-a3c7-ff95377ea0d7" />

---

## 🧠 Key Learning Outcomes

- Understanding web scraping basics

- Working with HTML parsing

- Handling relative vs absolute file paths

- Writing clean and readable Python code

- Real-world use of BeautifulSoup

---

## 🚀 Future Improvements

- Save data in CSV or JSON format

- Add error handling for missing elements

- Make the script reusable for other movie lists

- Add command-line arguments

---

## ✨ Author

**Bhavesh Vadnere**

📌 Engineering Student | Python Developer | AI & ML Enthusiast

GitHub: [BhaveshV23](https://github.com/BhaveshV23)

LinkedIn: [bhavesh-vadnere](https://linkedin.com/in/bhavesh-vadnere)
