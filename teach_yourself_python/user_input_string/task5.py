import time

def login():
    print("====LOGIN SCREEN===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "hello" and password == "open123":
        print("Access Granted")
        facebook()
    else:
        print("Access Denied")

def facebook():
    print("Welcome to Facebook")
    print("====You logged in succesfully!!!!======")
    print("Well... let other people understand more about you by answering these questions...")
    time.sleep(0.9)
    age = input("How old are you? >>> ")
    no_friends = input("How many friends do you have? >>> ")
    gender = input("And your gender is? >>> ")
    print("Thank you for confirming your age is {}, no of friends are {} and gender is {}.".format(age, no_friends, gender))

  
login()