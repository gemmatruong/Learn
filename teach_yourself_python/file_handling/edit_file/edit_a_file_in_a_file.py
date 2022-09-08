import csv
def main():

    updated_list = []
    temp_list = []
    
    with open("fakefacebook.txt", newline = "") as f:
        reader = list(csv.reader(f))
        print("CHANGE PASSWORD?!")
        username = input("Enter the username for the required user: ")
        temp_list = reader
        
        for row in reader:
            for field in row:
                if field == username:
                    updated_list.append(row)
                    new_password = input("Enter new password: ")
                    updated_list[0][1] = new_password
                
        
        update_password(updated_list, temp_list)
        
def update_password(updated_list, temp_list):
    for index, row in enumerate(temp_list):
        for field in row:
            if field == updated_list[0]:
                temp_list[index] = updated_list


    with open("fakefacebook.txt", "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerows(temp_list)
        print("File has been updated")


main()
