import csv

with open("fakefacebook.txt", newline = "") as f:
    reader = csv.reader(f)
    username = input("Enter username: ")
    for row in reader:
        if row[0] == username:
            print("{} has {} friends".format(username, row[3]))
