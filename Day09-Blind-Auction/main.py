from art import logo
import os
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    try:
        price = int(input("What is your bid?: $"))
    except ValueError:
        print("Please enter a valid number.")
        continue
    bids[name] = price
    while True:
        should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()

        if should_continue == "yes":
            os.system("cls" if os.name == "nt" else "clear")
            break
        elif should_continue == "no":
            continue_bidding = False
            winner, highest_bid = find_highest_bidder(bids)
            print(f"\nThe winner is {winner} with a bid of ${highest_bid}")
            break
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")