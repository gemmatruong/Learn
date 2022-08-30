def main():
    password = input("What is your password: ")
    if password == "open123":
        correct()
    else:
        for i in range(3):
            print("try again")
            password = input("Enter password again: ")
            if password == "open123":
                correct()
                break
        print("TOO MANY TRIES, SORRY?!")

def correct():
    print("yes, that's it")
    print("****** ACCESS GRANTED *********")
    print("congrats"*50, end = "")

main()
