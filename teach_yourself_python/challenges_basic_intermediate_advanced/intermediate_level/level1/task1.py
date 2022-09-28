import random

def main():
    print("================== WELCOME TO GUESSING SHOW ==================")
    name = input("Enter your name: ")
    print(f"Hi {name}, welcome to our show today. Your mission is to guess a lucky number...")
    print("...uhh.... let's begin right now!")
    guess()


def guess():
    lucky_num = random.randint(1,10)
    no_of_tries = 1
    correct = False
    while correct is False:
        player_num = int(input("Enter your guess: "))
        if player_num == lucky_num:
            if no_of_tries == 1:
                print("Woohoo, you find out the lucky number in the first time. Congratulations")
            else:
                print(f"Congratulation! You find out the lucky guess in {no_of_tries} tries")
            no_of_tries += 1
            correct = True
        else:
            print("Try again! Lucky number must be between 1 and 10")
            no_of_tries += 1

main()
