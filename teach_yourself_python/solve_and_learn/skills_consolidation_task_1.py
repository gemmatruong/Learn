def main():
    print("===========MAIN MENU==========")
    name = input("Student name: ")
    option = input("Enter subject option: ")
    print("Thanks, " + name + "! You have selected: " + option)

    if option in ["history", "History", "HISTORY"]:
        history()
    elif option in ["computing", "Computing", "COMPUTING"]:
        computing()
    else:
        print("Please make a valid selection")

def history():
    print("===== Welcome to History =====")
    correct = False
    for i in range(2):
        answer = input("Who is the first president of the US: ")
        if answer in ["George Washington", "george washington", "GEORGE WASHINGTON"]:
            print("Correct. A good start for beginner")
            correct = True
            break
        print("Sorry, not quite")
    if correct is False:
        print("...and sorry, it's the last try.")
    else:
        print("Good job")
        send_email()

def computing():
    print("===== Welcome to Computing =====")
    tries = 0
    correct = False
    while correct is False and tries < 2:
        answer = input("Name a programming language beginning with P: ")
        if answer in ["Python", "python", "PYTHON"]:
            print("Great - you are off to a good start")
            correct = True
            break
        print("Sorry, not quite")
        tries += 1
    if correct is False:
        print("...and sorry you are out of tries")
    else:
        print("Well done")
        send_email()

def send_email():
    email = input("==Please enter your email so we can send you subject details: ")
    if "@" in email:
        print("Valid email - and thanks")
        good_bye()
    else:
        print("Invalid email - try again")
        send_email()

def good_bye():
    for i in range(10):
        print("Goodbye ", end = "")


main()
