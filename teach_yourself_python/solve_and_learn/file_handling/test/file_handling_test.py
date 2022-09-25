import sys
import csv
import re

def mainmenu():
    print("""
====================== WELCOME TO TECHHAMPER.COM ========================
    |   1.-----Customer's Register                      |
    |   2.-----Customer's Login                         |
    |   3.-----Quit                                     |
    """)
    choice = input("Hi there, what would you like to do today? >>> ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        sys.exit()
    else:
        print("Please enter a valid choice")


def register():
    print("========== REGISTRATION ============")
    print("....Well you need to register for an account first")

    valid = False
    while valid is False:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username.isalpha():
            if re.search("[0-9]", password):
                fav_tech_product = input("Which tech product are you interested in? >>> ")
                valid = True
            else:
                print("Password must contain at least one number")
        else:
            print("Username can only contain alphabets.")
    
    with open("logininfo.txt", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow([username, password, fav_tech_product])
        print("Register successfully")
    
    mainmenu()


def login():
    print("=================== LOGIN =======================")
    with open("logininfo.txt", newline = "") as f:
        reader = list(csv.reader(f))
        valid = False
        while valid is False:
            username = input("Enter username: ")
            password = input("Enter password: ")
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Login successfully")
                    valid = True
                    print("Now... you have three options:")
                    print("|    1 >>> View tech products            |")
                    print("|    2 >>> Purchase your tech hamper     |")
                    print("|    3 >>> Manage your account           |")
                    print("|    3 >>> Quit                          |")

                    choice = input("Enter your choice: ")
                    if choice == "1":
                        view_tech_product(username)
                    elif choice == "2":
                        purchase_hamper(username)
                    elif choice == "3":
                        manage_account(username)
                    elif choice == "4":
                        sys.exit()
                    else:
                        print("Please make a valid choice")
            if valid is False:
                print("Invalid username or password. Try again")


def view_tech_product(username):
    print("****************** WELCOME *********************")
    products = {"cellphone": 500, "laptop": 1500, "smart watch": 450, "printer": 300, "speaker": 100, "TV": 3800, "Airtag": 50, "Earbuds": 270}
    print("These are our products: ", products)
    want_to_buy = "yes"
    while want_to_buy == "yes":
        tech_hamper = [username]
        product_name = input("Which item do you want to add to your hamper? If not, type 'no'>>> ")
        if product_name in products:
            tech_hamper.append(product_name)
            tech_hamper.append(products[product_name])
            print("Added to your hamper")

            with open("tech_hamper.txt", "a", newline = "\n") as f:
                writer = csv.writer(f)
                writer.writerow(tech_hamper)
        elif product_name == "no":
            print(">>>>> Thank you for experiencing with us")
            want_to_buy = "no"

        else:
            print("The item you enter was sold out")
    login()


def purchase_hamper(username):
    print("********** This is your tech hamper ************")
    recipient = input("You wanna checkout? First, give us the name of recipient: ")
    address = input("Then... the recipient's address: ")

    with open("deliveryinfo.txt", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow([username, recipient, address])
    print("You can checkout your tech hamper right now......")
    print("ORDER INFORMATION >>>>>>>>")
    total_cost = 0
    with open("tech_hamper.txt", newline = "") as f:
        reader = list(csv.reader(f))
        checkout_list = reader[1:]
        for row in checkout_list:
            if row[0] == username:
                total_cost += int(row[2])
                print(row)
        if total_cost == 0:
            print("There is no item in your hamper")
        else:
            print("Your total cost is: ", total_cost)
            checkout = input("Press enter to checkout >>> ")
    login()            


def manage_account(username):
    print("""
=========== THIS IS ACCOUNT MANAGEMENT ================
    |   1....View your account information                  |
    |   2....Delete an information record                   |
    |   3....Delete delivery information                    |
    |   4....Edit delivery information if it is incorrect   |
    """)
    valid = False
    while valid is False:
        choice = input("Enter your choice: ")
        if choice == "1":
            view_accountinfo(username)
            valid = True
        elif choice == "2":
            delete_record(username)
            valid = True
        elif choice == "3":
            delete_deliveryinfo(username)
            valid = True
        elif choice == "4":
            edit_info(username)
            valid = True
        else:
            print("Please make a valid choice")


def view_accountinfo(username):
    print("Hi there, this is your account information: ")

    account_info_list = [] 
    with open("logininfo.txt", newline = "") as f:
        reader = list(csv.reader(f))
        for row in reader:
            if username == row[0]:
                account_info_list.extend(row)
    
    with open("deliveryinfo.txt", newline = "") as f:
        reader = list(csv.reader(f))
        for row in reader:
            if username == row[0]:
                account_info_list.extend([row[1], row[2]])
    
    print("Username: {}\nPassword: {}\nFavorite tech product: {}\nDelivery info:\nRecipient: {}\nAddress: {}")


def delete_record(username):
    choice = input("You want to delete any information record? Press Enter to continue >>>")
    
    updatedlist = []
    with open("logininfo.txt", newline = "") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != username:
                updatedlist.append(row)
        print(updatedlist)
        update_records(updatedlist)
        
def update_records(updatedlist):
    with open("logininfo.txt", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(updatedlist)
        print("File has been updated")


def delete_deliveryinfo(username):
    choice = input("You want to delete any information record? Press Enter to continue >>>")
    
    updatedlist = []
    with open("deliveryinfo.txt", newline = "") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != username:
                updatedlist.append(row)
        print(updatedlist)
        update_delifile(updatedlist)
        
def update_delifile(updatedlist):
    with open("deliveryinfo.txt", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(updatedlist)
        print("File has been updated")


def edit_info():
    pass



mainmenu()