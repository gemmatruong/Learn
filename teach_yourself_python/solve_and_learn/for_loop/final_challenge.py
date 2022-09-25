def main():
    num = int(input("Please enter a number between 1 and 20: "))
    if num < 1 or num > 20:
        print("A number between 1 and 20 must be entered. Try again")
        main()
    else:
        for i in range(num + 1):
            print(i)


main()
