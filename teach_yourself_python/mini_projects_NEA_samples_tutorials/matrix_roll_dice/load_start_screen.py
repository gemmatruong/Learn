import sys


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
    else:
        sys.exit




main()
