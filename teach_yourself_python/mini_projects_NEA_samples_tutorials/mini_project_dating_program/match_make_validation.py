import time
import sys
import csv
import re

def main_menu():
    print("~~~~~  Welcome to HAPPY TOGETHER  ~~~~~")
    time.sleep(0.9)
    print("Our goal is to help you find out your destiny...")
    print("")
    time.sleep(1)
    print("Hi there... What are you gonna do today?")
    print("""    -- 1. Register
    -- 2. Login
    -- 3. Quit
    """)
    choose = False
    while not choose:
        user_choice = input()
        if user_choice == "1":
            register()
            choose = True
        elif user_choice == "2":
            login()
            choose = True
        elif user_choice == "3":
            print("Thank you for your visit! Have a good day...")
            time.sleep(1)
            print("Good bye!")
            sys.exit()
        else:
            print("You must enter an integer from 1 to 3")



def register():
    print("~~~~~~~~~~   REGISTER   ~~~~~~~~~~")
    print(">>> Wanna know if your love has been close to you?...")
    time.sleep(1.5)
    print("First, create your profile: ")

    with open("user_profile.txt", "a", newline = "") as fo:
        writer = csv.writer(fo)

        username = input("Create a unique username: ")

        # Check validation of password
        valid = False
        while not valid:
            password = input("Enter password: ")
            if len(password) >= 8:
                if re.search("[a-z]", password):
                    if re.search("[A-Z]", password):
                        if re.search("[0-9]", password):
                            if re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
                                valid == True
                                break
                            else:
                                print("Password must contain at least a special character")
                        else:
                            print("Password must contain at least one digit")
                    else:
                        print("Password must contain at least one uppercase")
                else:
                    print("Password must contain alphabet")
            else:
                print("Length of password must be at least 8 characters")


        first_name = input("We would like to know your first name: ")
        last_name = input("Your last name: ")
        gender = input("Gender: ")

        # Check validation of email
        valid_email = False
        while not valid_email:
            email = input("Enter your email address: ")
            if "@gmail.com" in email:
                valid_email = True
                break
            else:
                print("Email is not valid")


        # Check validation of date of birth
        date_valid = False
        while not date_valid:
            dob = input("Date of birth (mm/dd/yyyy): ")
            if 1 <= int(dob[:2]) <= 12 and dob[2] == "/" and dob[5] == "/" and 1 <= int(dob[3:5]) <= 31 and 1000 < int(dob[6:]) <= 2023:
                date_valid = True
                break
            else:
                print("Date must follow mm/dd/yyyy structure")


        beliefs = input("What is your belief? ")
        strengths_list = "determined, harworking, workaholic, innovative, energetic, organized, punctual, practical, honest, warmhearted, leader, independent"
        print(strengths_list)
        strengths = input("Tell us your greatest strength: ")

        writer.writerow([username, password, first_name, last_name, gender, email, dob, beliefs, strengths])
        print("profile saved!")

    main_menu()




def login():
    print("~~~~~~~~~~   LOGIN   ~~~~~~~~~~")
    print("You've already had an account? Login by your username and password...")
    access = False
    tries = 0
    while not access and tries < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        with open("user_profile.txt", "r") as fo:
            reader = csv.reader(fo)
            for line in reader:
                if line[0] == username and line[1] == password:
                    print("Access granted! Ready to find your love?~~~~")
                    access = True
                    break
            else:
                print("Try again")
                tries += 1
    if tries == 3:
        print("You only have 3 tries")

    print(">>>>> WELCOME TO DATING FORUM...")
    time.sleep(0.5)
    print("...Now you can freely search new friend and use match-make function to find out who suits you best...")
    time.sleep(0.5)
    print("""Please choose one: 
        >>> S - Search menu
        >>> M - Match make
        >>> Q - Quit
        """)
    choose = False
    while not choose:
        choice = input("")
        if choice in ["S", "s"]:
            search_menu()
            choose = True
        elif choice in ["M", "m"]:
            matchmake(username)
            choose = True
        elif choice in ["Q", "q"]:
            print("Good bye. Have a nice day!")
            sys.exit
        else:
            print("Please only type S or M to use function")


# Search function can be divided in 3 sections: by name, by gender, by keyword
def search_menu():
    print("Hi there, let's start finding your soulmate by searching feature...")
    time.sleep(1)
    search = input("Search: ")
    print("""You can:
    ~~~ 1. Search by Name
    ~~~ 2. Search by Gender
    ~~~ 3. Search by Key word
    ~~~ 4. Return main menu
    """)
    searching_choice = input("Search by: ")
    if searching_choice == "1":
        search_by_name(search)
    elif searching_choice == "2":
        search_by_gender(search)
    elif searching_choice == "3":
        search_by_keyword(search)
    else:
        main_menu()


def search_by_name(name):
    found = 0
    found_list = []
    with open("user_profile.txt", "r") as fo:
        reader = csv.reader(fo)
        for row in reader:
            for field in row:
                if field.capitalize() == name.capitalize():
                    found_list.append(row)
                    found += 1
                    break       # If found, break the loop to avoid returning the same user information
        if found == 0:
            print("0 result found")
        else:
            for ele in found_list: print(ele)
    search_menu()


def search_by_gender(name):
    # User friendly by typing first letter only
    sex_option = input("Type 'm' for male, 'f' for female: ")
    # Interpret gender
    if sex_option == "m":
        sex = "male"
    else:
        sex = "female"

    found = 0
    found_list = []     # List of result when matched name and gender
    sex_list = []       # List of result when matched gender only
    with open("user_profile.txt", "r") as fo:
        reader = csv.reader(fo)
        for row in reader:
            for field in row:
                # When user searchs a name, then choose to find a specific gender
                if field.capitalize() == name.capitalize():
                    if row[4] == sex:
                        found_list.append(row)
                        found += 1
                        break

            # Check if gender of data matches with gender user wants to find
            if row[4] == sex:
                sex_list.append(row[0])
        # When zero result found, print all users have the gender that has been searched
        if found == 0:
            for ele in sex_list: print(ele)
        else:
            for ele in found_list: print(ele)
    search_menu


def search_by_keyword(keyword):
    found = 0
    found_list = []
    with open("user_profile.txt", "r") as fo:
        reader = csv.reader(fo)
        for row in reader:
            for field in row:
                # Check if key word exists in any information of user
                if keyword in field:
                    found_list.append(row)
                    found += 1
                    break

        # When zero result found, print all users have the gender that has been searched        
        if found == 0:
            print("0 result found")
        else:
            for ele in found_list: print(ele)
    search_menu



def matchmake(user):
    print("Don't worry, your destiny is close to you...")
    time.sleep(0.5)
    print("...waiting...")
    print("...")
    time.sleep(1)


    # Open file, use username to get strength that user entered before
    with open("user_profile.txt", "r") as fo:
        reader = csv.reader(fo)
        for row in reader:
            if row[0] == user:
                user_characters = row[8]
                break

    # Couples are considered as two persons have complementary characteristics
    # Create a list of potential complementary characteristics
    complementary_couples = [["shy", "kind", "patience", "quiet"], ["outgoing", "energetic", "sociable", "friendly", "humorous", "hillarious"]], [["quick", "rush"], ["relaxed", "chill"]], [["organized", "clean", "neatly", "well-prepared", "time-managed", "punctual"], ["chaos", "clumsy", "enjoyed"]], [["listened", "warmhearted", "malleable"], ["independent", "leader", "determined"]], [["innovative", "creative", "smart", "intelligent"], ["hardworking", "workaholic", "stable", "happy"]]

    # Check all user information, if anyone harmonizes with the complementary condition, add to list of soulmates
    with open("user_profile.txt", "r") as fo:
        soulmates = []      # Create list of potential soulmates
        reader = csv.reader(fo)
        for row in reader:
            if row[0] != user:  # Avoid getting the user information
                object_char = row[8]    # Create a variable to get characteristic of each data
                for couple in complementary_couples:
                    if user_characters in couple[0]:    # Check if chacteristic is in complementary couples or not
                        if object_char in couple[1]:    # The same group of complementary couple can be soulmates
                            soulmates.append(row[0])
                    elif user_characters in couple[1]:
                        if object_char in couple[0]:
                            soulmates.append(row[0])

    if len(soulmates) == 0:
        print("Add more things about you to help us find out the best suit for you")
    else:
        print("This is the list of your potential soulmates: ")
        for mate in soulmates: print(mate)

    main_menu()




main_menu()
