def system():
    print("""=========== Welcome to our system ===========

    ....Please choose one option:

        Press 1. to register
        Press 2. to login
        Press 3. to quit
    """)
    choice = input("Enter number 1, 2 or 3 here: ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        quit()
    else:
        print("Only 1, 2 or 3 is accepted")

def register():
    print("This is register function")
    email = input("Enter your email: ")
    if '@' in email:
        password = input("Enter your password (must contain # in it): ")
        if "#" in password:
            print("Congratulations! Register successfully")
        else:
            print("Sorry, your password must include a #. Try again")
            print("")
            register()
    else:
        print("Sorry, your email must have an @. Try again")
        print("")
        register()

def login():
    print("This is login function")

def quit():
    quit = input("You want to quit? Enter to quit...")


system()
