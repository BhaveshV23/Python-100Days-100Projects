from art import logo, vs
from game_data import data
import random


def clear_screen():
    print("\n" * 20)


def format_data(account):
    """Return formatted account data for display."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_answer(guess, a_followers, b_followers):
    """Return True if guess is correct, else False."""
    if a_followers > b_followers:
        return guess == "a"
    return guess == "b"


def get_valid_guess():
    """Prompt user until a valid guess is entered."""
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess in ("a", "b"):
            return guess
        print("❌ Invalid input. Please type 'A' or 'B'.")


print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = get_valid_guess()

    clear_screen()
    print(logo)

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    if check_answer(guess, a_followers, b_followers):
        score += 1
        print(f"✅ You're right! Current score: {score}")
    else:
        print(f"❌ Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
