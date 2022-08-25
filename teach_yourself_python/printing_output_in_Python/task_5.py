#Bringing all our printing skills together

def facebook():
    name = input("Enter Name: ")
    print("")
    print("Hi " + name)
    print("")
    print("****      Welcome to Facebook    *****")
    print("""
        Press 1. to Register
        Press 2. to Login
        Press 3. to Signout

    """)
    press_enter = input("Press enter to continue:")
    profile(name)

def profile(name):
    print("=========== FACEBOOK PROFILE ===========")
    print("Welcome! " + name + " . What would you like to do?")
    print("""
        1. Search for other friends
        2. Post a message
        3. Post a picture
        4. Sign out
    """)
    print(name + ", have a good day!")
    print("")

facebook()

