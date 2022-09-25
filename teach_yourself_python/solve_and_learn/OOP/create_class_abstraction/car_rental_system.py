import sys

class CarRental:
    def __init__(self, dict_of_cars):
        self.avail_cars = list(dict_of_cars.keys())
        self.cost = list(dict_of_cars.values())

    def display_avail_cars(self):
        print("The cars we have in our system are as follows:")
        print("============================")
        for car in self.avail_cars:
            print(car)

    def rent_car(self, requested_car):
        if requested_car in self.avail_cars:
            no_of_days = int(input("How many days would you like to rent our car? >>> "))
            car_type = self.avail_cars.index(requested_car)
            cost_per_day = self.cost[car_type]
            total_cost = self.cost[car_type] * no_of_days
            print(f"Total rent cost is: {cost_per_day} x {no_of_days} = {total_cost} dolars")
            print("The car you requested has now been rented")
            self.avail_cars.remove(requested_car)
        else:
            print("Sorry the car you have requested is currently not in the company")

    def add_car(self, returned_car):
        self.avail_cars.append(returned_car)
        print("Thank you for returning your rented car")


class Customer:
    def __init__(self):
        self.car = None

    def request_car(self):
        print("Enter the name of the car you'd like to rent >>>")
        self.car = input()
        return self.car

    def return_car(self):
        print("Enter the name of the car you'd like to return >>>")
        self.car = input()
        return self.car

def main():
    rental_car = CarRental({"SUV": 10, "Sports": 100, "Hatchback": 200})
    customer = Customer()
    done = False
    while done is False:
        print(""" ============ GEMMA RENTAL CAR COMPANY ==================
        1. Display all available cars
        2. Request a car
        3. Return a car
        4. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            rental_car.display_avail_cars()
        elif choice == "2":
            rental_car.rent_car(customer.request_car())
        elif choice == "3":
            rental_car.add_car(customer.return_car())
        elif choice == "4":
            sys.exit()

main()
