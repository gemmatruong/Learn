import re

def main():
    stars = "*"*15
    print(stars + " Create an email address " + stars)
    print(stars + "                         " + stars)
    username = input("Please enter your desired username: ")
    if username.islower() and re.search("[0-9]", username):
        print("Your unique email address is now:", username + "@gmail.com")
    else:
        print("Your username needs to be lowercase and contain digits.......")


main()
