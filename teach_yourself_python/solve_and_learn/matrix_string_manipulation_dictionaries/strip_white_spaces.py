def main():
    password = input("What is your password? >>> ")
    password = "".join(char for char in password if char != " ")

    if password == "open123":
        print("Access granted")
    else:
        print("Sorry, access denied")


main()
