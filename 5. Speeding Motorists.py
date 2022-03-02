def integer_checker(question):
    error = "Sorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


speeder_name = input("Enter the name of the speeder: ").title()
speed_amount = integer_checker("Enter the amount over the speed limit: ")
