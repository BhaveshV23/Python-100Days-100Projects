# Day 08 – Caesar Cipher 🔐

A project from the 100 Days of Code – Python Pro Bootcamp by Dr. Angela Yu

## 📌 Description

The Caesar Cipher is one of the simplest encryption techniques. Each letter in a message is shifted by a user-defined number.
This project allows users to encode (encrypt) and decode (decrypt) messages using that shift value.

The program:

• Takes user input for message and shift

• Supports both encoding and decoding

• Preserves spaces, numbers, and punctuation

• Repeats until the user chooses to exit

## 🧠 How It Works

The Caesar Cipher shifts each alphabet letter by a fixed number.
For example, with a shift of 3:

a → d

x → a (wrap-around)

The project uses modulo (%) to cycle through the alphabet seamlessly.

## 📂 Project Structure
```
Day08-Caesar-Cipher/
│
├── main.py     # Main program containing the Caesar cipher logic
├── art.py      # ASCII logo displayed when the program runs
└── README.md   # Project documentation
```
## 💻 Features

• Encode and decode messages

• Handles large shifts using modulo wrap-around

• Maintains non-alphabet symbols

• User-friendly loop allowing multiple conversions

• Clean and organized function-based implementation

## 🧩 Code Overview
### caesar() Function

• Accepts the original text, shift amount, and mode (encode/decode)

• Reverses shift automatically for decoding

• Processes each character, shifting alphabet letters

• Builds and prints the final output

### Program Loop

• Continuously prompts user

• Stops only when user enters "no"

## ▶️ How to Run

1. Clone the repository:
```
git clone https://github.com/BhaveshV23/Python-100Days-100Projects
```

2. Navigate to the Day 08 project folder:
```
cd Day08-Caesar-Cipher
```

3. Run the program:
```
python main.py
```

## 🖼️ Sample Output
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
4
Here is the encoded result: lipps
Type 'yes' if you want to go again. Otherwise, type 'no'.
```
## 📘 Lessons Learned

• Using functions with parameters

• Applying modulo arithmetic

• Handling user input in loops

• Basic text manipulation

• Working with lists and string indexing

## ⭐ Future Improvements

• Add uppercase letter support

• Add colorized terminal output

• Create a GUI version

• Implement additional cipher methods (e.g., Vigenère Cipher)

## 🙏 Author

**Bhavesh Vadnere**

Python enthusiast | IT Engineering Student

GitHub: https://github.com/BhaveshV23
