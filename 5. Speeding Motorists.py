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
if speeder_name == "Zachary Conroy" or speeder_name == "James Wilson" \
        or speeder_name == "Helga Norman":
    speeder_name.upper()
    print(f"{speeder_name} - WARRANT TO ARREST")
speed_amount = integer_checker("Enter the amount over the speed limit: ")
if speed_amount < 10:
    print(f"{speeder_name} to be fined $30")
elif speed_amount <= 14:
    print(f"{speeder_name} to be fined $80")
elif speed_amount <= 19:
    print(f"{speeder_name} to be fined $120")
elif speed_amount <= 24:
    print(f"{speeder_name} to be fined $170")
elif speed_amount <= 29:
    print(f"{speeder_name} to be fined $230")
elif speed_amount <= 34:
    print(f"{speeder_name} to be fined $300")
elif speed_amount <= 39:
    print(f"{speeder_name} to be fined $400")
elif speed_amount <= 44:
    print(f"{speeder_name} to be fined $510")
else:
    print(f"{speeder_name} to be fined $630")
