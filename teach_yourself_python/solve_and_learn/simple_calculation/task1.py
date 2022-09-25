def convert_currency():
    pounds = int(input("Enter No. of Pounds: "))
    yen = pounds*150
    dollars = pounds*1.17
    print("Converted into yen, that would give you: ", yen)
    print("And that amount in dollars is: ", dollars)

convert_currency()