def main():
    stars = "*"*15
    print(stars + "REGISTER" + stars)
    print(stars + "        " + stars)
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    birth = input("Please enter your year of birth (e.g. 1999): ")
    print("Your unique username is: " + birth[2:] + last_name + first_name[0])

main()
