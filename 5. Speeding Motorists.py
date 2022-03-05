# checks if the input are integers not string or floats
def integer_checker(question):
    error = "Sorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# Displays a summary of the day
def summary_of_the_day():
    # Prints the total number of fines
    print(f"Total fines: {total_fines}")
    num = 0
    # Prints the names and amount over limit of the speeders
    for speed in speeder_list:
        new_num = num + 1
        print(f"{new_num}) Name: {speed[0]}   Amount over limit: {speed[1]}")
        num = num + 1
    # Prints the total amount of fines
    print(f"Total amount of fines: ${total_amount_of_fine:.2f}")


# Main routine
EXIT_SYMBOL = "X"
speeder_name = ""
speeder_list = []
total_fines = 0
total_amount_of_fine = 0
# While the user doesn't enter "x" when its asking for the speeder's name
while speeder_name != EXIT_SYMBOL:
    print("#" * 13)  # decoration
    # Asks for the name of the speeder who is getting a fine
    speeder_name = input("Enter the name of the speeder: ").title()
    if speeder_name == "X":
        print("#" * 13)
        summary_of_the_day()
    else:
        # If the speeder's name is Zachary Conroy, James Wilson or Helga Norman
        if speeder_name == "Zachary Conroy" or speeder_name == "James Wilson" \
         or speeder_name == "Helga Norman":
            # Changes speeder's name to all uppercase
            speeder_name = speeder_name.upper()
            # Prints that the following are wanted for arrest!
            print(f"{speeder_name} - WARRANT TO ARREST")
        # Asks for how much the speeder went over the speed limit
        speed_amount = integer_checker("Enter the amount over the speed "
                                       "limit: ")
        total_fines += 1  # adds 1 to the total number of fines
        # Adds the speeder's name and speed amount over limit to the list
        add_to_list = (speeder_name, speed_amount)
        speeder_list.append(add_to_list)
        # If amount over speed limit is less than 10
        if speed_amount < 10:
            # Then the speeder will be fined $30
            print(f"{speeder_name} to be fined $30")
            # Adds $30 to the total amount of fines
            total_amount_of_fine += 30
        # If amount over speed limit is less than or equal to 14
        elif speed_amount <= 14:
            # Then the speeder will be fined $80
            print(f"{speeder_name} to be fined $80")
            # Adds $80 to the total amount of fines
            total_amount_of_fine += 80
        # If amount over speed limit is less than or equal to 19
        elif speed_amount <= 19:
            # Then the speeder will be fined $120
            print(f"{speeder_name} to be fined $120")
            # Adds $120 to the total amount of fines
            total_amount_of_fine += 120
        # If amount over speed limit is less than or equal to 24
        elif speed_amount <= 24:
            # Then the speeder will be fined $170
            print(f"{speeder_name} to be fined $170")
            # Adds $170 to the total amount of fines
            total_amount_of_fine += 170
        # If amount over speed limit is less than or equal to 29
        elif speed_amount <= 29:
            # Then the speeder will be fined $230
            print(f"{speeder_name} to be fined $230")
            # Adds $230 to the total amount of fines
            total_amount_of_fine += 230
        # If amount over speed limit is less than or equal to 34
        elif speed_amount <= 34:
            # Then the speeder will be fined $300
            print(f"{speeder_name} to be fined $300")
            # Adds $300 to the total amount of fines
            total_amount_of_fine += 300
        # If amount over speed limit is less than or equal to 39
        elif speed_amount <= 39:
            # Then the speeder will be fined $400
            print(f"{speeder_name} to be fined $400")
            # Adds $400 to the total amount of fines
            total_amount_of_fine += 400
        # If amount over speed limit is less than or equal to 44
        elif speed_amount <= 44:
            # Then the speeder will be fined $510
            print(f"{speeder_name} to be fined $510")
            # Adds $510 to the total amount of fines
            total_amount_of_fine += 510
        # If amount over speed limit is higher than 44
        else:
            # Then the speeder will be fined $630
            print(f"{speeder_name} to be fined $630")
            # Adds $630 to the total amount of fines
            total_amount_of_fine += 630
