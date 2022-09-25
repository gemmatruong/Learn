def main():
    usernames = []
    passwords = []
    register(usernames, passwords)


def register(usernames, passwords):
    username = input("Enter a username: ")
    usernames.append(username)

    password = input("Enter a password: ")
    passwords.append(password)

    answer = input("Do you want to make another registration? >>> ")
    if answer == "y":
        register(usernames, passwords)
    else:
        registration_details(usernames, passwords)


def registration_details(usernames, passwords):
    print("List of usernames entered:", usernames)
    print("List of passwords entered:", passwords)


main()
