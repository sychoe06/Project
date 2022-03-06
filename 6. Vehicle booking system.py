# checks if the input are integers not string or floats
def int_checker(question):
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
    print("All vehicles that were booked today:")
    for b in booked_vehicles:
        print(f"\nVehicle number: {b[0]}\nVehicle type: {b[1]}\nName of"
              f"person who booked vehicle: {b[3]}")
    print("-" * 50)


# Main Routine
vehicles = [(1, "Suzuki Van", 2), (2, "Toyota Corolla", 4),
            (3, "Honda CRV", 4), (4, "Suzuki Swift", 4),
            (5, "Mitsubishi Airtrek", 4), (6, "Nissan DC Ute", 4),
            (7, "Toyota Previa", 7), (8, "Toyota Hi Ace", 12),
            (9, "Toyota Hi Ace", 12)]
booked_vehicles = []
EXIT_NUMBER = -1
seats_num = ""
num_vehicles = 9
while seats_num != EXIT_NUMBER:
    num_vehicles = len(vehicles)
    keep_going = "Yes"
    if num_vehicles == 0:
        seats_num = EXIT_NUMBER
    else:
        seats_num = int_checker("Enter number of seats needed in vehicle or "
                                "'-1' to exit: ")
        if seats_num == EXIT_NUMBER:
            end_of_the_day()
        else:
            print("-" * 5)
            print("Available Vehicles for booking:")
            for v in vehicles:
                if v[2] < seats_num:
                    print(f"\nCar Number: {v[0]}\nVehicle type: {v[1]}\nNumber"
                          f"of seats: {v[2]} - Not enough seats!")
                else:
                    print(f"\nCar Number: {v[0]}\nCar type: {v[1]}\nNumber of "
                          f"seats: {v[2]}")
            print("-" * 5)
            while keep_going == "Yes":
                vehicle_num = int_checker("Enter the vehicle number to book: ")
                for num in vehicles:
                    if vehicle_num == num[0] and seats_num > num[2]:
                        print(f"You cannot book vehicle number {vehicle_num} "
                              f"because there is not enough seats!\n")
                    elif num[0] == vehicle_num:
                        name = input("Enter your name: ").title()
                        booking = (num[0], num[1], num[2], name)
                        booked_vehicles.append(booking)
                        vehicles.remove(num)
                        print(f"Vehicle number {vehicle_num} has been booked!")
                        print()
                        keep_going = "No"
if num_vehicles == 0:
    end_of_the_day()
