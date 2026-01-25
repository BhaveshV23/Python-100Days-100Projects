import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (_, row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()

    # Remove spaces for validation
    cleaned_word = word.replace(" ", "")

    if not cleaned_word.isalpha():
        print("Sorry, only letters from A-Z are allowed.")
        continue

    output_list = [phonetic_dict[letter] for letter in cleaned_word]
    print(output_list)
    break