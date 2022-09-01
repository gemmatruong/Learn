def interview():
    print("=== WELCOME TO TECHSTARS INTERVIEW ===")
    print("")
    print("")
    print("Welcome! We'll begin with 3 questions for your interview")
    name = input("...but first, what is your name: ")
    score = 0
    q1 = input("Do you meet dealines? ")
    q2 = input("Are you hard working? ")
    q3 = input("Finally, do you know how to code? ")
    for i in [q1, q2, q3]:
        if i == "yes":
            score += 1
        else:
            score -= 1
    print(name, "your score is:", score)
    print("**********PROCESSING*********")
    print("")
    if score == 3:
        print("Taking you to the next level...")
        level_2()
    else:
        print("Sorry, but you have failed your interview. Goodbye!")        

def level_2():
    print("==== LEVEL 2 ======")
    print("You are about to be presented with a riddle: a sequence of numbers. You need to predict what comes next? ")
    for i in range(2, 10, 2):
        print(i)
    
    tries = 0
    correct = False
    while tries < 3 and correct is False:
        answer = input("What comes next? >>> ")
        if answer == "10":
            print("Well done... you're through to the next level...")
            correct = True
            break
        print("Nope...")
        tries += 1
    if correct is False:
        print("Sorry, you are no longer being interviewed - Goodbye!")
    else:
        level_3()


def level_3():
    print("==== LEVEL 3 ======whooop")
    print("You are about to be presented with another riddle: a sequence of numbers. You need to predict what comes next? ")
    for i in range(1, 12, 2):
        print(i)  

    tries = 0
    correct = False
    while tries < 3 and correct is False:
        answer = input("What comes next? >>> ")
        if answer == "13":
            print("Great! Congratulations... THE JOB IS YOUR!!! continue to the most difficult level")
            correct = True
            break
        print("Nope...")
        tries += 1
    if correct is False:
        print("Sorry, you are no longer being interviewed.")
        print("============= GOOD BYE =============")
    else:
        final_level()


def final_level():
    print("==== FINAL LEVEL ======WOW")
    print("This is the Fibonacci sequence of numbers. You need to predict what comes next? ")
    for row in range(3, 11):
        for col in range(1, row):
            print(Fibonacci(col), end = ", ")
        print("")
    
    tries = 0
    correct = False
    while tries < 3 and correct is False:
        answer = input("What comes next? >>> ")
        if answer == "55":
            print("Great! Congratulations... You truly have the job")
            print("CONGRATS "*10, end = "")
            correct = True
            break
        print("Nope...")
        tries += 1
    if correct is False:
        print("Sorry, you are no longer being interviewed.")
        print("============= GOOD BYE =============")

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


interview()
