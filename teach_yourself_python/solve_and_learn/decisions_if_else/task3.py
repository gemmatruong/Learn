def cars():
    expensive_cars = ["Mercedes", "Audi", "BMW", "Tesla", "Lexus"]
    cheap_cars = ["Skoda", "Maruthi", "Nano", "Toyota", "Kia", "Hyundai"]

    budget = int(input("How much can you spend on a car? >>> "))
    if budget >= 5000:
        print("Here are some cars you could consider", expensive_cars)
    else:
        print("You may want to check out these brands: ", cheap_cars)


cars()