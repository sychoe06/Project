def integer_checker(question):
    error = ">> Sorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def welcome_screen():
    print("-" * 70)
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below.")
    print("-" * 70)
    print("1 Drop off a child\n2 Pick up a child\n3 Calculate cost\n"
          "4 Print Roll\n5 Exit the system\n")


def drop_off():
    name = input("Enter the name of the child: ").title()
    name_list.append(name)
    print(name, "has been added to the list")


def pickup():
    if num_children == 0:
        print(">> Sorry there are currently no children in MGS childcare "
              "to be picked up")
    else:
        name = input("Enter the name of the child: ").title()
        if name in name_list:
            name_list.remove(name)
            print(name, "has been removed from the list")
        else:
            print(">> Sorry we cannot find a child with the name of", name,
                  "at MGS childcare")


def calc_cost():
    if num_children == 0:
        print(">> Sorry there are currently no children in MGS childcare.\n"
              ">> So there is no cost to calculate.")
    else:
        hours = integer_checker("Enter the number of hours to charge: ")
        cost = 12
        charge = hours * cost * num_children
        print(f"Charge is ${charge:,.2f}")


def print_roll():
    if num_children == 0:
        print("Currently there are no children who are "
              "checked at MGS Childcare")
    elif num_children == 1:
        print("Currently there is only", num_children, "child who is checked "
                                                       "in at MGS Childcare:")
        for child in name_list:
            print(child)
    else:
        print("Currently there are", num_children, "children who are checked "
                                                   "in MGS Childcare:")
        for children in name_list:
            print(children)


choice = 0
name_list = []
while choice != 5:
    num_children = len(name_list)
    welcome_screen()
    choice = integer_checker("Enter your choice (number between 1-5): ")
    print()
    if choice == 1:
        drop_off()
    elif choice == 2:
        pickup()
    elif choice == 3:
        calc_cost()
    elif choice == 4:
        print_roll()
    elif choice >= 6 or choice == 0:
        print(">> Sorry! Enter a number between 1-5! Please try again\n")
    else:
        print(">> Goodbye! Thank you for coming to MGS Childcare")
