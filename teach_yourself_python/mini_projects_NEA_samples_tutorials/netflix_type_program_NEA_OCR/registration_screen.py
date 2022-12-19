import sys
import time
import csv
import re


def main():
    time.sleep(0.5)
    print("")
    print("~~~~~~~~~~~~ WELCOME TO GREEN GEM ~~~~~~~~~~~~")
    print("...Great experience in watching films and series on GREEN GEM...")
    time.sleep(0.5)
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
    email = input("Email: ")
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
    pass

main()
