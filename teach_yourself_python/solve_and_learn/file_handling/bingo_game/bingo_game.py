import random
import sys
import csv

def mainmenu():
    print("""
=================== MAIN MENU ======================
+-----------------====------------------------------+
|    1........... Play game                         |
|    2........... View players and scores record    |
|    3........... Quit                              |
    """)
    choice = input("What do you want to do? >>> ")
    if choice == "1":
        play_game()
    elif choice == "2":
        view_records()
    elif choice == "3":
        sys.exit()
    else:
        print("Oh no! Please make valid choice")


def play_game():
    bingo = random.randint(1, 20)
    name = input("Enter your full name here: ")
    print("Hi", name, "....Now, let's start to guess the bingo number.....")

    # Use while loop to ask player guess until bingo
    correct = False
    tries = 0
    while correct is False:
        num = int(input("Which number have you guessed? >>> "))
        tries += 1
        if num == bingo:
            print("Bingo! Congratulation!!!!!!!!!!!!")
            print("You can bingo in", tries, "tries!!!!!")
            correct = True
        else:
            print("Try again")

    # Add player's record to file
    with open("players_records.txt", "a", newline = "\n", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, tries])
    mainmenu()


def view_records():
    with open("players_records.txt", newline = "\n", encoding="utf-8") as fi:
        reader = csv.reader(fi)
        reader = list(reader)
        # Column title does not need to sort, so print title separately
        print(reader[0])

        # Sort the tries of players from lowest no.of tries first
        sorted_list = list(reader[1: len(reader)])
        sorted_list.sort(key = lambda x:int(x[1]))
        for row in sorted_list:
            print(row)
    mainmenu()


mainmenu()
