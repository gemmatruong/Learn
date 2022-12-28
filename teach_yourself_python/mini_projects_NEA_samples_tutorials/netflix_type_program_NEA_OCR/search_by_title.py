import sys
import time
import csv
import re


def main():
    print("")
    print("~~~~~~~~~~~~ WELCOME TO GREEN GEM ~~~~~~~~~~~~")
    print("...Great experience in watching films and series on GREEN GEM...")
    choice = input("""
        1 - Sign up
        2 - Login
        3 - Logout
    Enter choice here: """)

    if choice == "1":
        registration()
    elif choice == "2":
        login()
    elif choice == "3":
        sys.exit
    else:
        print("Please only type 1, 2 or 3")
        print("Try again!")
        main()


def registration():
    username = input('Enter a unique username: ')
    valid = False
    while not valid:
        password = input("Enter password: ")
        if len(password) >= 8:
            if re.search("[a-z]", password):
                if re.search("[A-Z]", password):
                    if re.search("[0-9]", password):
                        if re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
                            valid = True
        
        if valid == False:
            print("""You must create a password whose minimum length is 8 characters.
Password contains at least 1 alphabet, 1 uppercase, 1 digit, 1 special character
""")

    firstname = input("First name: ")
    lastname = input("Last name: ")
    gender = input("Enter your gender: ")
    dob = input("Enter your date of birth (mm/dd/yyyy): ")
    address = input("Enter your address: ")

    correct_email = False
    while not correct_email:
        email = input("Email: ")
        if "@" in email:
            correct_email = True
        else:
            print("Invalid email")
            print("Try again!")
            print("")


    payment = input("""Choose how to pay:
        a - Credit or Debit Card
        b - PayPal
        c - Gift Code from Green Gem
    Enter here: """)
    if payment == "a":
        payment = "Credit or Debit Card"
    elif payment == "b":
        payment = "PayPal"
    elif payment == "c":
        payment == "Gift Code"

    plan = input("""Choose plan that you want: 
        a - Basic with ads: $6.99  -  good video quality   -  720p
        b - Standard:       $15.49 - better video quality  - 1080p
        c - Premium:        $19.99 -  best video quality   - 4K+HDR
        Enter here: """)
    if plan == "a":
        plan = "Basic with ads"
    elif plan == "b":
        plan = "Standard"
    elif plan == "c":
        plan = "Premium"

    with open("greengem_file.txt", "a", newline = "") as fi:
        writer = csv.writer(fi)
        writer.writerow([username, password, firstname, lastname, gender, dob, address, email, payment, plan])
    print("profile saved!")
    main()



def login():

        valid = False
        tries = 0
        while not valid and tries < 3:
            with open("greengem_file.txt", "r") as fo:
                reader = csv.reader(fo)
                global username
                username = input("Enter username: ")
                password = input("Enter password: ")
                for row in reader:
                    if row[0] == username and row[1] == password:
                        print("Access Granted!")
                        valid = True
                        films_menu()
                        break
                if valid == False:
                    print("Incorrect username or password...Try again!")
                    tries += 1
                if tries >= 3:
                    print("Exceed 3 tries!")
                    main()


def films_menu():
    print(" ~~~~~~~~~~~~~~ WELCOME TO GREEN GEM ~~~~~~~~~~~~~~ ")
    print("...Hi there, what would you like to do? ")
    choice = input("""
            W - Watch a films
            V - View your playlist (liked list)
            T - Search by Title
            R - Search by Rating
            Q - Quit Green Gem
    Enter choice here: """)
    
    if choice in ["W", "w"]:
        watch_films()
    elif choice in ["V", "v"]:
        view_playlist()
    elif choice in ["T", "t"]:
        search_by_title()
    elif choice in ["R", "r"]:
        search_by_rating()
    elif choice in ["Q", "q"]:
        sys.exit()
    else:
        print("You must only select from the given options")
        print("Try again!")
    films_menu()


def watch_films():
    with open("films_list.txt", "r") as fo:
        reader = csv.reader(fo)
        for row in reader:
            print(row)
    
    print("What would you like to do?")
    choice = input("""
            Select a number to view film
                or:
            R: Return to the Main Menu
            Q: Quit Green Gem
        Please enter your choice here: """)

    if choice in ["R", "r"]:
        films_menu()
    elif choice in ["q", "Q"]:
        sys.exit
    elif choice == "1":
        film_viewing(1)
    elif choice == "2":
        film_viewing(2)
    elif choice == "3":
        film_viewing(3)
    elif choice == "4":
        film_viewing(4)
    elif choice == "5":
        film_viewing(5)
    elif choice == "6":
        film_viewing(6)
    elif choice == '7':
        film_viewing(7)
    elif choice == '8':
        film_viewing(8)
    elif choice == '9':
        film_viewing(9)
    elif choice == '10':
        film_viewing(10)
    elif choice == '11':
        film_viewing(11)
    elif choice == '12':
        film_viewing(12)
    elif choice == '13':
        film_viewing(13)
    elif choice == '14':
        film_viewing(14)
    elif choice == '15':
        film_viewing(15)
    elif choice == '16':
        film_viewing(16)
    elif choice == '17':
        film_viewing(17)
    elif choice == '18':
        film_viewing(18)
    elif choice == '19':
        film_viewing(19)
    elif choice == '20':
        film_viewing(20)
    else:
        print("Please choose from the given options")
        print("Try again!")
        watch_films()



def film_viewing(n):
    print("Waiting...")
    with open("films_list.txt", "r") as fo:
        films_list = csv.reader(fo)
        for film in films_list:
            if film[0] == str(n):
                watched_list = [film[0], film[1], film[2], film[4]]
                print("You're watching the movie", film[2])
                break

    # Store watched film in a file according to username. Each username has a watched films file
    with open("%s.txt" %username, "a", newline = "") as fi:
        writer = csv.writer(fi)
        writer.writerow(watched_list)
        print("Your recent watched list has been created!")


    # Create like function for viewers
    print("You like this film? ^^ ")
    choice = input("""
        If yes, press L 
            or you want:
                W - Watch another film
                R - Return to main films menu
                Q - Quit Green Gem
        Enter choice here: """)
    
    if choice in ["L", "l"]:
        like_a_film(n)
    elif choice in ["W", "w"]:
        watch_films()
    elif choice in ["r", "R"]:
        films_menu()
    elif choice in ["q", "Q"]:
        sys.exit()


def like_a_film(n):
    with open("films_list.txt", "r") as fo:
        reader = csv.reader(fo)
        films_list = [row for row in reader]
    
    for film in films_list:
        if film[0] == str(n):
            film[-1] = str(int(film[-1]) + 1)

    with open("films_list.txt", "r") as fi:
        writer = csv.writer(fi)
        writer.writerow(films_list)
        print("liked!")
        watch_films()




def view_playlist():
    pass


def search_by_title():
    result = 0
    search = input("""
    Enter FILM TITLE to search
        or choose:
            R - to return to main film menu
            Q - Quit Green Gem

    Enter here: """)

    if search in ["R", "r"]:
        films_menu()
    elif search in ["q", "Q"]:
        sys.exit()
    else:
        with open("films_list.txt", "r") as fo:
            reader = csv.reader(fo)
            for row in reader:
                if search.capitalize() in row[2].capitalize():
                    print(row)
                    result += 1
            if result != 0:
                choice = input("""
    Enter the number of film that you wanna watch right now (If no film as your wish, type NO) >>> """)
                if choice in ["NO", "no", "No"]:
                    search_by_title()
                elif choice.isdigit():
                    film_viewing(int(choice))



def search_by_rating():
    pass



main()
