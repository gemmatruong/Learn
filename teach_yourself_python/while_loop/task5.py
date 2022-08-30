import time

def main():
    health = 100
    gameover = False
    while gameover == False and health >= 0:
        print("The game is on.....")
        print("Your health is down to:", health)
        time.sleep(1.1)
        health = health - 10
    print("YOU LOSE")


main()