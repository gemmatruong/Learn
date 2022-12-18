"""
Create a search feature and report that lists all the females in the file
with their corresponding addresses
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
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~ WELCOME TO MAIN MENU ~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(0.5)

    choice = input(""" 
    You can choose one of these actions:
        ~ 1. Enter students details
        ~ 2. View all students details
        ~ 3. Search student details
        ~ 4. Produce reports menu
        ~ 5. Quit
    What do you want to do? """)


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
        time.sleep(1)
        menu()




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
    time.sleep(0.5)

    # Teacher can produce reports according to these purpose:
    # 1/ Sending anouncement about soccer tournament amongs boys: list of males and email addresses
    # 2/ Sending cards and gifts on March 8th: list of females and home addresses
    # 3/ Sending emergent messages: list of all students and phone numbers

    choice = input("""
        What kind of report do you wanna get?
            a - Soccer tournaments: list of males and email addresses
            b - March 8th events: list of females and home addresses
            c - Emergencies: list of all students and phone numbers
            d - Menu
            e - Quit
        Enter choice here: """)

    if choice in ["a", "A"]:
        soccer_tournaments()
    elif choice in ["b", "B"]:
        women_events()
    elif choice in ["c", "C"]:
        emergencies()
    elif choice in ["d", "D"]:
        menu()
    elif choice in ["e", "E"]:
        sys.exit
    else:
        print("You can only choose one of five options")
        print("Try again!")
        time.sleep(1)
        produce_reports_menu()

    cont = input()
    produce_reports_menu()


def soccer_tournaments():
    print("The biggest soccer tournament of our school is coming...")
    time.sleep(0.4)
    print("Send all boys new anouncements to have them into this event...")
    time.sleep(0.2)
    print("")

    with open("students_details.txt", "r") as fo:
        found = 0
        reader = csv.reader(fo)
        for row in reader:
            if row[6] == "male":
                print(row[0], "-" ,row[1], "- email:", row[8])
                found += 1

    print(found, "results found")


def women_events():
    print("Ready for the International Women's Day?...")
    time.sleep(0.4)
    print("Get all the girls' addresses and send them gift with love...")
    time.sleep(0.2)
    print("")

    with open("students_details.txt", "r") as fo:
        found = 0
        reader = csv.reader(fo)
        for row in reader:
            if row[6] == "female":
                print(row[0], "," ,row[1], ", address:", row[4])
                found += 1

    print(found, "results found")



def emergencies():
    pass



form_tutor_login()
