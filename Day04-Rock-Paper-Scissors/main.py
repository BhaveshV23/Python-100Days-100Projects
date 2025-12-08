import random
print("Welcome to Rock, Paper, and Scissors Game!")
user_choice = int(input('Enter 1 for "rock", 2 for "paper", and 3 for "scissors"'))
computer_choice = random.randint(1,3)
print(computer_choice)
if user_choice > 3 or user_choice < 1:
    print("Wrong Input!")
if user_choice == computer_choice:
    print("It's a tie!")
elif (computer_choice == 1 and user_choice == 2) or (computer_choice == 2 and user_choice == 3) or (computer_choice == 3 and user_choice == 1):
    print("You win!")
else:
    print("Computer win!")