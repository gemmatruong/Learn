def guess_number():
    for i in range(1, 11):
        guess = input("I'm thinking of a number from 1 to 10, can you guess what it is? >>> ")
        if guess == "7":
            print("Well done! You guessed the number in", i, "attempt[s]!")
            break
        else:
            print("Try again!")
    else:
        print("No try more!")


guess_number()
