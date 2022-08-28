def main():
    access = False
    while access == False:
        password = input("Enter secret password: ")
        if password == "open123":
            access = True
  
    print("Access Granted")
main()