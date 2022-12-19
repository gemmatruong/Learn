import sys
import time


def main():
    time.sleep(0.3)
    print("")
    print("~~~~~~~~~~~~ WELCOME TO GREEN GEM ~~~~~~~~~~~~")
    print("...Great experience in watching films and series on GREEN GEM...")
    time.sleep(0.3)
    choice = input("""
        1 - Sign up
        2 - Login
        3 - Quit
    Enter choice here: """)

    if choice == "1":
        registration()
    elif choice == "2":
        login()
    elif choice == "3":
        sys.exit
    else:
        print("Please only type 1, 2 or 3")
        print("Try again!")
        main()


def registration():
    pass


def login():
    pass

main()
