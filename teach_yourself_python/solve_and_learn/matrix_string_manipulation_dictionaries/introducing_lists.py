def main():
    subject = input("Hello, what course are you finding out about? >>> ")
    if subject in ["maths", "computing", "history"]:
        print("We still have spaces on the:", subject, "course")
        name = input("So, please could you tell us your name? >>> ")
        print("Thank you")
        hw = input("Do you always do your homework? >>> ")
        if hw in ["yes", "YES", "Yes", "of course", "absolutely", "always", "I do"]:
            print(name, ".... we would be very pleased to have you on our course")
        else:
            print("I'm sorry,", name, "...but hw is import, and therefore we reverse judge")
    else:
        print("Oh so sorry, we do not have more space for", subject, "course")


main()
