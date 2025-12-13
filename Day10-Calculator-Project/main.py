import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    """Safely get a valid float from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid number. Please enter a valid numeric value.")


def get_operation():
    """Safely get a valid operation symbol."""
    while True:
        op = input("Pick an operation: ").strip()
        if op in operations:
            return op
        print("❌ Invalid operation. Choose from +, -, *, /.")


def calculator():
    print(art.logo)

    num1 = get_number("What is the first number?: ")

    while True:
        for symbol in operations:
            print(symbol)

        operation_symbol = get_operation()
        num2 = get_number("What is the next number?: ")

        try:
            answer = operations[operation_symbol](num1, num2)
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")
            continue

        print(f"✅ {num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue with {answer}, 'n' for new calculation, or 'q' to quit: "
        ).lower()

        if choice == "y":
            num1 = answer
        elif choice == "n":
            print("\n" * 2)
            calculator()
            return
        elif choice == "q":
            print("👋 Calculator closed.")
            return
        else:
            print("❌ Invalid choice. Exiting calculator.")
            return


calculator()
