def age_and_hours():
    age = int(input("What is your age?: "))
    if age>12:
        print("You are old!")
    else:
        print("Wow...your whole life ahead of you")
    hours = int(input("Enter the no. of hours you spend on homework per week: "))
    if hours>10:
        print("Wow - you do a lot of independent study!")
    else:
        print("...are you sure that's enough to help you get ahead?!")


age_and_hours()