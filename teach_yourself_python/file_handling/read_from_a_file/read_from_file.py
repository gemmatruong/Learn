import csv

with open("studentinfo.txt", newline = "") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
