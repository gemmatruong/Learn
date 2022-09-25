def main():
    access = False
    while access == False:
        password = input("Enter password to continue: ")
        if password == "open123":
            access = True
        else:
            print("Denied")
    print("Access granted")
    quiz()

def quiz():
    print("""****************** WELCOME ******************
The wonderful world of learning Python awaits.....
""")
    i = 1
    while i <= 2:
        answer = input("What was the first name of the man who created Python? >>> ")
        if answer in ["guido", "Guido", "GUIDO"]:
            print("Whoop-Correct")
            break
        print("Ah...nope.")
        if i == 2:
            print("....and that's it. Good bye - there are consequences for getting things wrong!")
        i += 1


main()