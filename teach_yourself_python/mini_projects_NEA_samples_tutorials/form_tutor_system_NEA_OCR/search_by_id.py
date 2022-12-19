"""
In this task you need to create a SEARCH BY ID feature. The form tutor or
use should be able to put in an ID number, and the student record (i.e. all
the details for that student) should be displayed on the screen
"""


import time
import sys
import csv


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
    with open("students_details.txt", "a", newline = "") as fo:
        writer = csv.writer(fo)
        id = input("Enter ID: ")
        firstname = input("First name: ")
        lastname = input("Last name: ")
        dob = input("Date of birth: ")
        address = input("Home address: ")
        phone_num = input("Phone number: ")
        gender = input("Gender: ")
        tutor_group = input("Tutor group: ")
        school_email = input("School email address: ")
        writer.writerow([id, firstname, lastname, dob, address, phone_num, gender, tutor_group, school_email])
    print("profile saved!")
    print("")



def view_all_details():
    print(">>>>> VIEW ALL STUDENTS DETAILS <<<<<")
    with open("students_details.txt", "r") as fo:
        reader = csv.reader(fo)
        ss_list = list(reader)
        print("Our school has {} students".format(len(ss_list)))
        for row in ss_list:
            print(row)



def search_by_ID():
    print(">>>>> SEARCH STUDENTS DETAILS BY ENTERING ID <<<<<<")
    id = input("Enter ID: ")
    with open("students_details.txt", "r") as fo:
        reader = csv.reader(fo)
        found = False
        for row in reader:
            if row[0] == id.title():
                print(row)
                found = True
                break
        if found == False:
            print("Incorrect ID!")



def produce_reports_menu():
    print(">>>>> REPORT MENU <<<<<")


form_tutor_login()
