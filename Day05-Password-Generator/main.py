import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_digits = int(input("How many digits would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(letters))

for i in range(nr_digits):
    password_list.append(random.choice(numbers))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("Your Password is", password)