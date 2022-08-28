import time
def password():
    password = input("Enter password to continue: ")
    if password == "open123":
        main()
    else:
        print("Sorry, you appear to be an imposter! Access denied")

def main():
    print("*********************WELCOME**************************")
    title = input("How can I call you? (Ms, Mr or Mrs?) -")
    name = input("Hello " + title + ". What is your name? -")
    print("What a lovely name... " + title + " " + name)
    age = int(input("Please enter your age: "))
    if age < 18:
        print("Sorry, you are too young")
    else:
        quiz()

def quiz():
    print("""***************WELCOME TO THE QUIZ***************
    >>> Let's start your very first question. Good luck
    .....loading....
    """)
    time.sleep(0.9)
    print(">>> Time flies >>>")
    time.sleep(0.9)
    print("Thank you. Wish you all the best")


password()
