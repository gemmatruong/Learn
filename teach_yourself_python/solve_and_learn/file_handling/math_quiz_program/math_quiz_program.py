import random
import csv
import re

def mainmenu():
    print("""
========================= MAIN MENU =============================
    """)
    valid = False
    while valid is False:
        name = input("Hi there, what is your name? >>> ")
        if re.search("[0-9]", name):
            print("Invalid name! Try again, without any numbers")
        else:
            print("Great!.... Let's start the quiz")
            valid = True
            quiz(name)


def quiz(name):
    print("""
*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*
=================== WELCOME TO QUIZ SHOW ========================
....>>> You have to answer 3 mathematical questions.
....Each correct answer, you will get 10 points.
>>>>>> GOOD LUCK !
""")
    scores = 0

    # Use for loop to control how many questions player will be asked
    for q in range(3):
        # Randomly generate questions
        operator = random.choice(["+", "-", "x"])
        first_num = random.randint(0, 9)
        second_num = random.randint(0, 9)

        # Declare the correct answer for each operator being used
        if operator == "+":
            correct_answer = first_num + second_num
        elif operator == "-":
            correct_answer = first_num - second_num
        else:
            correct_answer = first_num * second_num

        # Collect the answer from player by input() function and convert answer into integer
        player_answer = int(input("What is {} {} {}? >>> ".format(first_num, operator, second_num)))

        # Check whether answer of player is correct, if correct, score increase 10
        if player_answer == correct_answer:
            print("That's right")
            scores += 10
            print("Well... Your score is", scores)
            print("")
        else:
            print("Not quite, sorry! The answer is ", correct_answer)

    if scores > 10:
        print("Well done! You are very good at math")
    else:
        print("Don't worry! Try harder next time")

    with open("scores.txt", "a", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, scores])


mainmenu()
