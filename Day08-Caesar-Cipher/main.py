import art
import string
print(art.logo)

alphabet = string.ascii_lowercase

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    return output_text

def ask_to_restart():
    while True:
        choice = input("Type 'yes' to go again or 'no' to exit:\n").lower()

        if choice == "yes":
            return True
        elif choice == "no":
            print("Goodbye 👋")
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ("encode", "decode"):
        print("Invalid choice.")
        continue

    text = input("Type your message:\n").lower()
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Shift must be a number.")
        continue

    output = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    print(f"Here is the {direction}d result: {output}")

    if not ask_to_restart():
        break

