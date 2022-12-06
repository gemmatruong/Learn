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
    pass


def login():
    pass


def search():
    pass


def matchmake():
    pass


main_menu()
