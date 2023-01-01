import sys
import random


def main():
    print("~~~~~~~~~~~~~~~~ ROLL DICE ~~~~~~~~~~~~~~~~")
    load_start_screen()


# Create a matrix with dimension n
def grid(n):
    lst = []
    for i in range(7):
        if i % 2 == 0:
            lst.append([j for j in range(n * i + 1, n * i + n + 1)])
        elif i % 2 == 1:
            lst.append([j for j in range(n * i + n, n * i, -1)])
    lst.reverse()
    return lst

def print_matrix(n):
    for ele in grid(n):
        print(ele)


def load_start_screen():
    print("Two players: ")
    global player1, player2
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")

    print("Welcome " + player1 + " and " + player2 + "... Are you ready???")
    ready = input("Yes or No? Type here to confirm: ")
    if ready in ["YES", "Yes", "yes", "yEs", "yeS", "YEs", "YeS", "yES", "y", "Y"]:
        enter = input("ROLL DICE game is about to start. Press ENTER to continue...")
        print_matrix(7)
        roll_dice()
    else:
        sys.exit


def roll_dice():
    print("~~~~~~~~~~~~~~~~ GAME STARTS ~~~~~~~~~~~~~~~~~~~~~")
    sum1 = 0
    sum2 = 0
    playing = True
    while playing:
        # Player 1 's turn
        player1_turn = input("Player 1, it's your turn. Press r to roll the dice: ")
        if player1_turn == "r" or "R":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            sum1 += dice1 + dice2
            # pos1 = sum1 - 1
            print("You rolled a " + str(dice1) + " and a " + str(dice2) + " which give you a: " + str(sum1))
            playing, message = win_check(sum1, playing)
            if playing == False:
                print(message)
                break
            print("---------------------------")
            enter = input("Press ENTER to continue...")

            # Player 2 's turn
            player2_turn = input("Player 2, it's your turn. Press r to roll the dice: ")
            if player2_turn == "r" or "R":
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                sum2 += dice1 + dice2
                # pos2 = sum2 - 1
                print("You rolled a " + str(dice1) + " and a " + str(dice2) + " which give you a: " + str(sum2))
                playing, message = win_check(sum1, playing)
                if playing == False:
                    print(message)
                    break
                print("---------------------------")
                enter = input("Press ENTER to continue...")
            else:
                sys.exit
        else:
            sys.exit
        # lst = grid(7)
        # lst[]
            
def win_check(sum, playing):
    if sum == 49:
        playing = False
        message = "You win! Congratulation!"
        return playing, message
        


main()
