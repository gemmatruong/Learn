import csv


with open('fakefacebook_write.txt', 'a', newline = "\n") as fo:
    Writer = csv.writer(fo)
    id = input("Enter ID: ")
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    no_of_likes = input("Enter number of likes: ")
    Writer.writerow([id, firstname, lastname, username, password, email, no_of_likes])
    print("Record has been written to file")
