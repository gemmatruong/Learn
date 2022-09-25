""" ==============TASK
1. Add an ID number to the file (e.g. 001, 002, and so on for each user)
2. Search by ID number, and return the whole record of the user

e.g.
Search by ID: 001
>>"Whole profile for 001:" --001,Ruth,Marvin,marvR,marv@gmail.com,200
"""

import csv

ID = ["ID","001", "002", "003", "004"]
with open("fake_facebook_with_names.txt", "r") as f, \
        open("output_file", "w", newline = "") as fo:
    reader = csv.reader(f)
    writer = csv.writer(fo)
    x = 0
    for row in reader:
        row.insert(0, ID[x])
        writer.writerow(row)
        x += 1


with open("output_file", newline = "") as f:
    reader = csv.reader(f)
    entered_ID = input("Enter ID: ")
    for row in reader:
        if row[0] == entered_ID:
            for ele in row:
                if ele == row[len(row)-1]:
                    print(ele)
                else:
                    print(ele, end = ",")
