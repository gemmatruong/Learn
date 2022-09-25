import sys
import csv

def mainmenu():
    print("""
===================== MAIN MENU =======================""")
    print("+-------------------------------------------------+")
    print("|  Please select an option:                      |")
    print("| 1 - Register                                   |")
    print("| 2 - Login                                      |")
    print("| 3 - Quit                                       |")
    print("----------------------------------------")
    choice = input("What would you like to do? >>> ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice =="3":
        sys.exit()
    else:
        print("Please enter valid choice")


def register():
    print("================ REGISTRATION =============")
    print("You need an account to join in magic program.....")
    username = input("Enter an username: ")
    password = input("Enter a password: ")

    with open("logininfo.txt", "a", newline = "\n", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])

    print("Congratulation! Successful registration")
    
    mainmenu()


def login():
    print("================ LOGIN =============")
    valid = False
    while valid is False:
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("logininfo.txt", newline = "\n", encoding = "utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Logic successfully")
                    print("Now, it's time to enjoy magic program....")
                    valid = True
                    magic()
            if valid is False:
                print("Invalid username or password. Try again")


def magic():
    #solution to modulo arithemetic magic using lists
    print("============= WELCOME TO MODULO ARITHMETIC===================")
    print("****** We're here to help you solve your problem*************")
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    entered_day = input("Enter day of week: ")
    entered_number = input("Enter no. of days: ")
    day_pos_in_days = days.index(entered_day)
    print(days[(day_pos_in_days + int(entered_number)) % 7])
    mainmenu()


mainmenu()
