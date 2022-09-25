import csv
def main():
    updatedlist = []
    with open("fakefacebook.txt", newline = "") as f:
        reader = csv.reader(f)
        username = input("Enter the username of the user you wish to remove from file: ")

        for row in reader:
            if row[0] != username:
                updatedlist.append(row)
        print(updatedlist)
        updatefile(updatedlist)
        
def updatefile(updatedlist):
    with open("fakefacebook.txt", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(updatedlist)
        print("File has been updated")
        

main()
