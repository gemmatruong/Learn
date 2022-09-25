import time
def option_select():
    print("Answer the question to see if you are eligible to join the course:")
    hw = input("Do you do your homework? >>> ")
    effort = input("Do you always put in a 100% effort? >>> ")
    attend = input("Does your attendance is always good (could be 100%)? >>> ")
    if hw == "yes" and effort == "yes" and attend == "yes":
        print("We'd love to have you on the course")
    else:
        print("Not sure about you on this course. Sorry!")
    print("")
    time.sleep(0.9)
    email()

def email():
    email = input("We would like your email address for our records, Please enter it: ")
    if "@" in email:
        print("That is a valid email. Enter to continue")
        enter = input()
        ID_number()
    else:
        print("That doesn't appear to be a valid e-mail. Try again")
        email()

def ID_number():
    ID_num = input("Enter your ID number here, please: ")
    if ID_num.startswith("07"):
        print("We got your ID, thank you")
    else:
        print("The ID number you entered is invalid, try again")
        ID_number()


option_select()