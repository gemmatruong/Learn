import time
import sys
import csv

def main_menu():
    print("~~~~~  Welcome to HAPPY TOGETHER  ~~~~~")
    time.sleep(0.9)
    print("Our goal is to help you find out your destiny...")
    print("")
    time.sleep(2)
    print("Hi there... What are you gonna do today?")
    print("""    -- 1. Register
    -- 2. Login
    -- 3. Search
    -- 4. Matchmake
    -- 5. Quit
    """)
    user_choice = input()
    if user_choice == "1":
        register()
    elif user_choice == "2":
        login()
    elif user_choice == "3":
        search()
    elif user_choice == "4":
        matchmake()
    elif user_choice == "5":
        print("Thank you for your visit! Have a good day...")
        time.sleep(2)
        print("Good bye!")
        sys.exit()
    else:
        print("You must enter an integer from 1 to 5")



def register():
    print("~~~~~~~~~~   REGISTER   ~~~~~~~~~~")
    print(">>> Wanna know if your love has been close to you?...")
    time.sleep(1.5)
    print("First, create your profile: ")

    with open("user_profile.txt", "a", newline = "") as fo:
        writer = csv.writer(fo)

        username = input("Create a unique username: ")
        password = input("Enter password: ")
        first_name = input("We would like to know your first name: ")
        last_name = input("Your last name: ")
        gender = input("Gender: ")
        email = input("Enter your email address: ")
        dob = input("Date of birth (mm/dd/yyyy): ")
        beliefs = input("What is your belief? ")
        strengths_list = "determined, harworking, workaholic, innovative, energetic, organized, punctual, practical, honest, warmhearted, leader, independent"
        print(strengths_list)
        strengths = input("Tell us three of your greatest strengths (separated by a hyphen '-' ): ")

        writer.writerow([username, password, first_name, last_name, gender, email, dob, beliefs, strengths])
        print("profile saved!")
    
    main_menu()


def login():
    print("~~~~~~~~~~   LOGIN   ~~~~~~~~~~")
    print("You've already had an account? Login by your username and password...")
    access = False
    tries = 0
    while not access and tries < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("user_profile.txt", "r") as fo:
            reader = csv.reader(fo)
            for line in reader:
                if line[0] == username and line[1] == password:
                    print("Access granted! Ready to find your love?~~~~")
                    access = True
                    break
            else:
                print("Try again")
                tries += 1
    if tries == 3:
        print("You only have 3 tries")
    
    main_menu()


def search():
    pass


def matchmake():
    pass


main_menu()
