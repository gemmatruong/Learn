"""
Create a login screen. Define a function (call it "login"). The form tutor should be
able to use username:formtutor and password: teacherypass to access the system.
Show a message which says "Access Granted" if the credentials entered are correct
"""
import time
import sys


def form_tutor_login():
    access = False
    while not access:
        username = input("Username: ")
        password = input("Password: ")

        if username == "formtutor" and password == "teacherypass":
            print("Access Granted")
            menu()
            access = True
        else:
            print("Try again")



def menu():
    print("~~~~~~~~~~~~~~~~~~~~~ WELCOME TO MAIN MENU ~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    print(""" 
    You can choose one of these actions:
        ~ 1. Enter students details
        ~ 2. View all students details
        ~ 3. Search student details
        ~ 4. Produce reports menu
        ~ 5. Quit
    """)

    valid_choice = False
    while not valid_choice:
        choice = input("What do you want to do? ")

        if choice == "1":
            enter_details()
        elif choice == "2":
            view_all_details()
        elif choice == "3":
            search_by_ID()
        elif choice == "4":
            produce_reports_menu()
        elif choice == "5":
            print("Good bye! Have a nice day...")
            sys.exit()
        else:
            print("Please enter an integer from 1 to 5")



def enter_details():
    print(">>>>> ENTER AND SAVE STUDENTS DETAILS <<<<<")



def view_all_details():
    print(">>>>> VIEW ALL STUDENTS DETAILS <<<<<")



def search_by_ID():
    print(">>>>> SEARCH STUDENTS DETAILS BY ENTERING ID <<<<<<")



def produce_reports_menu():
    print(">>>>> REPORT <<<<<")
    # Teacher can produce reports according to these purpose:
    # 1/ Sending anouncement about soccer tournament amongs boys: list of males and email addresses
    # 2/ Sending cards and gifts on March 8th: list of females and home addresses
    # 3/ Sending emergent messages: list of all students and phone numbers




form_tutor_login()
