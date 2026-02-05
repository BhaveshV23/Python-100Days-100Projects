import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_digits = int(input("How many digits would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = (
    [random.choice(letters) for _ in range(nr_letters)] +
    [random.choice(numbers) for _ in range(nr_digits)] +
    [random.choice(symbols) for _ in range(nr_symbols)]
)

random.shuffle(password_list)

password = "".join(password_list)

print("Your Password is", password)