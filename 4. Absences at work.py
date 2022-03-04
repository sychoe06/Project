# checks if the input are integers not string
def integer_checker(question):
    error = "Sorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# Calculates and displays the final data of the absences of employees
def calc_absences():
    print("-" * 70)  # decoration
    # If the total number of absent days is 0 then...
    if total_absent_days == 0:
        # The average number of days of absence per year is 0
        print("Average number of days staff were absent:\t0\n")
        # The average number of days of absence per year is 0
        print(f"Person with most absent days: \t\t\t\tnone\n")
        print("List of people not absent at all:")
        print("\t" * 11 + "none")
        print("\nList of people absent above average:")
        print("\t" * 11 + "none")
    # But if the total number of absent days is higher than 0 then it...
    else:
        # Calculates the average number of days of absence per year
        average_absent_days = total_absent_days / num_employee
        # Prints the average number of days of absence per year
        print(f"Average number of days staff were absent:\t"
              f"{average_absent_days:.2f}\n")
        # Prints the name of the employee who had the most days of absence
        print(f"Person with most absent days:\t\t\t\t{most_absent_person} with"
              f" {most_absent_days} days\n")
        print("List of people not absent at all:")
        # Sorts list of employees (who were not absent) in alphabetical order
        not_absent_people_list.sort()
        # Prints out the employees who were not absent at all during the year
        for people in not_absent_people_list:
            print("\t" * 11 + people)
        # Sorts the list of all employees in alphabetical order
        employee_list.sort()
        # List of employees who are over the average number of absence days
        employee_over_average = []
        print("\nList of people absent above average:")
        for employee in employee_list:
            # Only adds in the employee to the list if...
            # the employee's absent days is bigger than the average number
            if employee[1] > average_absent_days:
                employee_over_average.append(employee)
        # Prints the employees who are over the average number of absence days
        for over_average in employee_over_average:
            print(over_average[0], over_average[1])
            if len(over_average[0]) < 3:
                print("\t" * 11 + over_average[0], "\t\t\t\t", over_average[1])
            elif len(over_average[0]) <= 6:
                print("\t" * 11 + over_average[0], "\t\t\t", over_average[1])
            elif len(over_average[0]) < 11:
                print("\t" * 11 + over_average[0], "\t\t", over_average[1])
            else:
                print("\t" * 11 + over_average[0], "\t", over_average[1])
    print("-" * 70)  # decoration


# Main routine
employee_list = []
not_absent_people_list = []
most_absent_days = 0
total_absent_days = 0
most_absent_person = ""
employee_name = ""
EXIT_SYMBOL = "$"
# Keep asking for employee names and absent days
while employee_name != "$":
    # Keeps count of the number of employees in the list
    num_employee = len(employee_list)
    # Asks for employee's name
    employee_name = input(f"Enter the name of the employee or "
                          f"'{EXIT_SYMBOL}' to exit: ").title()
    # If the "exit symbol" is entered then the while loop ends
    if employee_name == "$":
        # Calls the function
        calc_absences()
    # If the employee's name is entered then code carries on like normal
    else:
        # Asks for the number of days the employee was absent
        absent_days = integer_checker(f"Enter the number of days "
                                      f"{employee_name} was absent: ")
        # Adds the employee's name and absent days into a variable
        absent_employee = (employee_name, absent_days)
        # Then adds that variable to the list
        employee_list.append(absent_employee)
        # Adds the absent days to the total number of absent days
        total_absent_days += absent_days
        # If the employee's absent days is higher than the most absent days...
        if absent_days > most_absent_days:
            # Then the most absent person changes to this new employee
            most_absent_person = employee_name
            # And the most absent days changes to this new absent days
            most_absent_days = absent_days
            print()  # adds a line of spacing
        elif absent_days == 0:
            # If employee's absent days is 0 then the employee is...
            # added to the list of people who were never absent
            not_absent_people_list.append(employee_name)
            print()  # adds a line of spacing
        else:
            print()  # adds a line of spacing


