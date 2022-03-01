def integer_checker(question):
    error = "Sorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def end_of_the_day():
    print("-" * 50)
    if total_time == 0:
        print(f"The Driver's name: {driver_name}\n"
              f"Total time of all trips: 0 minutes\n"
              f"Average time of all trips: 0 minutes\n"
              f"Total income for the day: $0.00\n"
              f"Average cost of all trips: $0.00")
    else:
        average_time = total_time / total_trips
        average_cost = total_income / total_trips
        if total_time == 1:
            print(f"The Driver's name: {driver_name}\n"
                  f"Total time of all trips: {total_time} minute\n"
                  f"Average time of all trips: {average_time:.0f} minute\n"
                  f"Total income for the day: ${total_income:.2f}\n"
                  f"Average cost of all trips: ${average_cost:.2f}")
        else:
            print(f"The Driver's name: {driver_name}\n"
                  f"Total time of all trips: {total_time} minutes\n"
                  f"Average time of all trips: {average_time:.0f} minutes\n"
                  f"Total income for the day: ${total_income:.2f}\n"
                  f"Average cost of all trips: ${average_cost:.2f}")
    print("-" * 50)


# Main routine
BASE_COST = 10
COST_PER_MINUTE = 2
trip = ""
total_trips = 0
total_time = 0
total_income = 0
driver_name = input("What is the driver's name? ")
while trip != "N":
    trip = input("\nWould you like to start a new trip?\n"
                 "Enter Y for Yes or N for No: ").upper()
    if trip == "Y":
        minutes = integer_checker("\nEnter how many minutes the trip tooK: ")
        cost = BASE_COST + COST_PER_MINUTE * minutes
        total_trips += 1
        total_income += cost
        total_time += minutes
    elif trip == "N":
        end_of_the_day()
    else:
        print("\nPlease enter either 'Y' or 'N'! Try again!\n")
