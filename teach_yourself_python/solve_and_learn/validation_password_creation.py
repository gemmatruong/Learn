import re
import sys
from random import*


def password():
    valid = False
    while valid == False:
        password = input("Create a password: ")
        if 6 <= len(password) <= 12:
            other_checks(password, valid)
        else:
            print("Password length between 6 and 12 please")
            print("Not a valid password")

def other_checks(password, valid):
    if re.search("[0-9]", password):
        if re.search("[A-Z]", password):
            if re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
                print("Valid Password")
                valid == True
                sys.exit()
            else:
                print("You need at least one special character please")
        else:
            print("You need at least one upper case character")
    else:
        print("You need at least one number in password")
    print("Not a valid password")


password()
