"""
Create a login screen. Define a function (call it "login"). The form tutor should be
able to use username:formtutor and password: teacherypass to access the system.
Show a message which says "Access Granted" if the credentials entered are correct
"""
import time

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
    time.sleep(0.5)


form_tutor_login()
