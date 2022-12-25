import sys
import time
import csv
import re


def main():
    print("")
    print("~~~~~~~~~~~~ WELCOME TO GREEN GEM ~~~~~~~~~~~~")
    print("...Great experience in watching films and series on GREEN GEM...")
    choice = input("""
        1 - Sign up
        2 - Login
        3 - Logout
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
    username = input('Enter a unique username: ')
    valid = False
    while not valid:
        password = input("Enter password: ")
        if len(password) >= 8:
            if re.search("[a-z]", password):
                if re.search("[A-Z]", password):
                    if re.search("[0-9]", password):
                        if re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
                            valid = True
        
        if valid == False:
            print("""You must create a password whose minimum length is 8 characters.
Password contains at least 1 alphabet, 1 uppercase, 1 digit, 1 special character
""")

    firstname = input("First name: ")
    lastname = input("Last name: ")
    gender = input("Enter your gender: ")
    dob = input("Enter your date of birth (mm/dd/yyyy): ")
    address = input("Enter your address: ")

    correct_email = False
    while not correct_email:
        email = input("Email: ")
        if "@" in email:
            correct_email = True
        else:
            print("Invalid email")
            print("Try again!")
            print("")


    payment = input("""Choose how to pay:
        a - Credit or Debit Card
        b - PayPal
        c - Gift Code from Green Gem
    Enter here: """)
    if payment == "a":
        payment = "Credit or Debit Card"
    elif payment == "b":
        payment = "PayPal"
    elif payment == "c":
        payment == "Gift Code"

    plan = input("""Choose plan that you want: 
        a - Basic with ads: $6.99  -  good video quality   -  720p
        b - Standard:       $15.49 - better video quality  - 1080p
        c - Premium:        $19.99 -  best video quality   - 4K+HDR
        Enter here: """)
    if plan == "a":
        plan = "Basic with ads"
    elif plan == "b":
        plan = "Standard"
    elif plan == "c":
        plan == "Premium"

    with open("greengem_file.txt", "a", newline = "") as fi:
        writer = csv.writer(fi)
        writer.writerow([username, password, firstname, lastname, gender, dob, address, email, payment, plan])
    print("profile saved!")
    main()



def login():
    with open("greengem_file.txt", "r") as fo:
        reader = csv.reader(fo)
        valid = False
        tries = 0
        while not valid and tries < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Access Granted!")
                    valid = True
                    films_menu()
                    break
            if valid == False:
                print("Incorrect username or password...Try again!")
                tries += 1
            if tries >= 3:
                print("Exceed 3 tries!")
                main()


def films_menu():
    print(" ~~~~~~~~~~~~~~ WELCOME TO GREEN GEM ~~~~~~~~~~~~~~ ")
    print("...Hi there, what would you like to do? ")
    choice = input("""
            W - Watch a films
            V - View your playlist
            T - Search by Title
            R - Search by Rating
            Q - Quit Green Gem
    Enter choice here: """)
    
    if choice in ["W", "w"]:
        watch_films()
    elif choice in ["V", "v"]:
        view_playlist()
    elif choice in ["T", "t"]:
        search_by_title()
    elif choice in ["R", "r"]:
        search_by_rating()
    elif choice in ["Q", "q"]:
        sys.exit()
    else:
        print("You must only select from the given options")
        print("Try again!")
        films_menu()


def watch_films():
    pass


def view_playlist():
    pass


def search_by_title():
    pass


def search_by_rating():
    pass



main()
