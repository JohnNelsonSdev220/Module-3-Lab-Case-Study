# File Name: Mod 3 Case Study.py
#Student: John Nelson
#Description: Accept user inputs for various car questions such as the year and model, it should only accept certain answers for certain questions such as how many doors there are either 2 or 4, nothing else should be accepted. Then it will print the output.



class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def user_input():
    vehicle_type = "car"
    while True:
        year = input("Enter the year: ")
        if year.isdigit():
            break
        print("Please enter a valid numeric year.")
    make = input("Enter the make: ")
    model = input("Enter the model: ")

    while True:
        doors = input("Enter either 2 or 4 doors: ")
        if doors in ["2", "4"]:
            break
        print("Incorrect input. Please enter 2 or 4.")

    while True:
        roof = input("Enter either 'solid' or 'sun roof': ").lower()
        if roof in ["solid", "sun roof"]:
            break
        print("Incorrect input. Please enter 'solid' or 'sun roof'.")

    return Automobile(vehicle_type, year, make, model, doors, roof)


    return Automobile(vehicle_type, year, make, model, doors, roof)

def display_vehicle_info(auto):
    print("\nVehicle Information:")
    print(f"  Vehicle type: {auto.vehicle_type}")
    print(f"  Year: {auto.year}")
    print(f"  Make: {auto.make}")
    print(f"  Model: {auto.model}")
    print(f"  Number of doors: {auto.doors}")
    print(f"  Type of roof: {auto.roof}")

def main():
    car = user_input()
    display_vehicle_info(car)

if __name__ == "__main__":
    main()