try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid input. Please enter a number.")
    age = int(input("How old are you?"))

if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print("You are not old enough to drive.")

# Debugging method:
# - Used try/except
# - Prevented program crash
