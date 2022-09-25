import sys

def main_menu():
    print("""
    ************************* == WELCOME == *************************
        Press P  to Play
        Press A  to find out more about the quiz
        Press Q to Quit
---------------------------------
""")
    choice = input("Please enter your selection: ")
    if choice == "P" or choice == "p":
        quiz()
    elif choice == "A" or choice == "a":
        information()
    else:
        sys.exit()

def quiz():
    print("""***************** WELCOME TO THE QUIZ **************************
........ready to play?!
**********************************************************************""")
    score = 0
    q1 = input("What is the last book of the Bible that also talks about the end of the world? >>> ")
    if q1 in ["revelation", "Revelation", "REVELATION"]:
        print("Correct")
        score += 20
        print("Your score is", score)
        question_2(score)
    else:
        print("Sorry, not quite! Back to the start for you!")
        quiz()

def question_2(score):
    q2 = input("How many commandments are there? >>> ")
    if q2 in ["10", "ten", "Ten", "TEN"]:
        print("Good job")
        score += 20
        print("Your score is", score)
        question_3(score)
    else:
        print("Oh no, not correct, back to the start for you!")
        quiz()

def question_3(score):
    q3 = input("When did Jesus rise from the dead? >>> ")
    if q3 in ["Easter Sunday", "Easter", "easter sunday", "easter", "EASTER SUNDAY"]:
        print("Well-done")
        score += 20
        print("Your score is", score)
        question_4(score)
    else:
        print("Sorry, it's incorrect. Back to the start for you!")
        quiz()

def question_4(score):
    q4 = input("For how many days was Jesus in the tomb? >>> ")
    if q4 == "3":
        print("Excellent")
        score += 20
        print("Your score is", score)
        question_5(score)
    else:
        print("Sorry, try harder next time. Back to the start for you!")
        quiz()

def question_5(score):
    q5 = input("Where did Jesus grow up? >>> ")
    if q5 == "Nazareth":
        print("Wonderful! Your memory is perfect")
        score += 20
        print("Your score is", score)
    else:
        print("It's not quite. Sorry. Back to the start for you!")
        quiz()

def information():
    print("""
    About the quiz
    This quiz is going to have 5 questions and will be on the Bible.
    Each correct answer, you will get 20 scores.
    **********************************************************************
    """)


main_menu()
