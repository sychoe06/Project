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
    # calculating average number of days of absence per year
    average_absent_days = total_absent_days / num_employee
    # printing out average number of days of absence per year
    print(f"Average number of days staff were absent:\t"
          f"{average_absent_days:.2f}\n")
    # printing out the name of the employee who had the most days of absence
    print(f"Person with most days absent:\t\t\t\t{most_absent_person} with "
          f"{most_absent_days} days\n")
    print("List of people not absent at all:")
    # Sorts the list of employees (who were not absent) in alphabetical order
    not_absent_people_list.sort()
    for people in not_absent_people_list:
        print("\t" * 10 + "	" + people)
    # Sorts the list of all employees in alphabetical order
    employee_list.sort()
    # List of employees who are over the average number of absence days
    employee_over_average = []
    print("\nList of people absent above average:")
    for employee in employee_list:
        if employee[1] > average_absent_days:
            employee_over_average.append(employee)
    for over_average in employee_over_average:
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
while employee_name != "$":
    num_employee = len(employee_list)
    employee_name = input(f"Enter the name of the employee or "
                          f"'{EXIT_SYMBOL}' to exit: ").title()
    if employee_name == "$":
        calc_absences()
    else:
        absent_days = integer_checker(f"Enter the number of days "
                                      f"{employee_name} was absent: ")
        absent_employee = [employee_name, absent_days]
        employee_list.append(absent_employee)
        total_absent_days += absent_days
        if absent_days > most_absent_days:
            most_absent_person = employee_name
            most_absent_days = absent_days
            print()
        elif absent_days == 0:
            not_absent_people_list.append(employee_name)
            print()
        else:
            print()
