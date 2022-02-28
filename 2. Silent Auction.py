# checks if the input are numbers not string
def number_checker(question):
    error = "Sorry, you must enter a number\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


# checks if the highest bid beats the reserve price
def check_reserve_price():
    # if highest bid beats the reserve price then it prints out the highest bid
    if reserve_price <= highest_bid:
        print("\nThe auction for the sloth finished with a bid of "
              f"${highest_bid:.2f}")
    # if highest bid does not beat the reserve price then it does not sell
    else:
        print(f"\nThe {item_being_auctioned} did not sell")


# Main routine
highest_bid = 0
bid = 0
# Asks for what object is being put up for auction
item_being_auctioned = input("What is the auction for? ")
# Asks for the reserve price from the auction manager before the auction starts
reserve_price = number_checker("What is the reserve price? ")
print(f"\nThe auction for the {item_being_auctioned} has started!\n")

# Keeps asking for a bid until -1 is entered to stop the while loop
while bid != -1:
    # Keeps letting the user know what the highest bid is
    print(f"Highest bid so far is ${highest_bid:.2f}")
    # asks user for their bid
    bid = number_checker("What is your bid? ")
    # if the bid is higher than the highest bid...
    if bid > highest_bid:
        # then it changes the highest bid to the bid
        highest_bid = bid
    # if the user enters -1...
    elif bid == -1:
        # then it calls the check reserve price function to end the code
        check_reserve_price()
    # However if the bid is lower than the highest bid then...
    else:
        # Then it asks the user to enter a higher bid
        print("Please enter a higher bid")
