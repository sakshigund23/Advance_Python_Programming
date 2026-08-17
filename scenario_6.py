class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Category:", self.category())
        print("------------------------")


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added successfully!")

    def display_all(self):
        if len(self.vehicles) == 0:
            print("No vehicles available.")
        else:
            print("\n--- All Vehicles ---")
            for vehicle in self.vehicles:
                vehicle.display()


# Main Program
showroom = Showroom()

while True:
    print("\n===== Vehicle Showroom Management System =====")
    print("1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = input("Enter Vehicle Number: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))

        vehicle = Vehicle(number, brand, price)
        showroom.add_vehicle(vehicle)

    elif choice == 2:
        showroom.display_all()

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")


# OUTPUT:
# ===== Vehicle Showroom Management System =====
# 1. Add Vehicle
# 2. Display All Vehicles
# 3. Exit
# Enter your choice: 1
# Enter Vehicle Number: MH12AB1234
# Enter Brand: Toyota
# Enter Price: 800000
# Vehicle added successfully!
#
# ===== Vehicle Showroom Management System =====
# 1. Add Vehicle
# 2. Display All Vehicles
# 3. Exit
# Enter your choice: 1
# Enter Vehicle Number: MH14CD5678
# Enter Brand: BMW
# Enter Price: 1500000
# Vehicle added successfully!
#
# ===== Vehicle Showroom Management System =====
# 1. Add Vehicle
# 2. Display All Vehicles
# 3. Exit
# Enter your choice: 2
#
# --- All Vehicles ---
# Vehicle Number: MH12AB1234
# Brand: Toyota
# Price: 800000.0
# Category: Economy
# ------------------------
# Vehicle Number: MH14CD5678
# Brand: BMW
# Price: 1500000.0
# Category: Luxury
# ------------------------
#
# ===== Vehicle Showroom Management System =====
# 1. Add Vehicle
# 2. Display All Vehicles
# 3. Exit
# Enter your choice: 3
# Thank you!