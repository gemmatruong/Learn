usernames_passwords = {"user1": "pass1", "user2": "pass2", "user3": "pass3"}

def main():
    print("""****** MAIN MENU ********
========Press L to login: 
========Press R to register: 
""")
    choice = input()
    if choice == "L" or choice == "l":
        login()
    elif choice == "R" or choice == "r":
        register()
    else:
        print("Only L or R is valid.")


def login():
    print("*******LOGIN SCREEN*******")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    if username not in usernames_passwords:
        print("Username does not exist")
    elif usernames_passwords[username] == password:
        print("Great! Access granted")
    else:
        print("Sorry - wrong password")


def register():
    print("******REGISTRATION*******")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    other = input("Do you want to make another registration? >>> ")
    usernames_passwords[username] = password

    if other == "y":
        register()
    else:
        print(usernames_passwords)

main()
