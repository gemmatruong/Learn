#If you want to write lots of text you can use triple speech marks

def main():
    print("""
    ================MAIN MENU================
    Press P to Play Game
    Press V to View Scores
    Press S to Save Scores
    Press Q to Quit


    """)
    playgame()
  
def playgame():
    print("===You are now in the game menu====")
    print("Welcome")
    print("""
    >>> Easy ways to play tic tac toe here:

    1. First player is X, another one is O.
    2. Put your mark on empty squares.
    3. Players take turn to play.
    4. The first player gets 3 of her marks in a row is the winner.
    
    Let's start <<<
    """)

main()