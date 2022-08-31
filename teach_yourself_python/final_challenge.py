import sys

def main():
    option = input("Do you prefer to add or subtract? >>> ")
    if option == "add":
        add()
    else:
        subtract()

def add():
    print("*** QUESTION THAT INVOLVES THE TEDIUS BUSINESS OF ADDING *******")
    for i in range(3):
        answer = input("What is 4 + 4: ")
        if answer == "8":
            print("Congratulations")
            print("*"*500, end = "")
            print("")
            sys.exit()
        else:
            print("Sorry, Wrong")
    print("You have had too many tries to answer this difficult question. How sad! Good bye!")

def subtract():
    print("*** A TERRIBLY HARD QUESTION ON SUBTRACTION ********")
    for i in range(3):
        answer = input("What is 5 - 2: ")
        if answer == "3":
            print("Congratulations")
            print("*"*500, end = "")
            print("")
            sys.exit()
        else:
            print("Sorry, Wrong")


main()
