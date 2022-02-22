def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
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
    name = input("Enter the name of the child: ")
    name_list.append(name)
    print(name, "has been added to the list")


def pickup():
    name = input("Enter the name of the child: ")
    if name in name_list is True:
        name_list.remove(name)
        print(name, "has been removed from the list")
    else:
        print("Please check the child's name because they are not on the list")


choice = 0
name_list = []
while choice != 5:
    welcome_screen()
    choice = integer_checker("Enter your choice (number between 1-5): ")
    if choice == 1:
        drop_off()
    elif choice == 2:
        pickup()




