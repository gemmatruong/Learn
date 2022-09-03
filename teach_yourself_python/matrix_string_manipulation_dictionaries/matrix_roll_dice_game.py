import sys

def matrix_list():
    lst = []
    x = 1
    for row in range(6, 31, 5):
        ele = []
        for col in range(x, row):
            col = str(col)
            ele.append(col)
        x += 5
        lst.append(ele)
    return lst


def main():
    # Create list
    lst = matrix_list()
    for ele in lst:
        print(ele)

    # Ask name
    name = input("Enter a letter that will be your player name: ")
    print("Thank you", name)

    # Change all value of lst into "*"
    for ele in lst:
        for i in range(5):
            ele[i] = "*"

    # Use while loop to check whether the position of player is the end of lst
    pos = 0
    while pos != 24:
        num = int(input("Please enter a number from 1 to 5: "))
        pos += num
        if pos > 24:
            print("Game lose")
            sys.exit()
        else:
            print("Well done, " + name + "! You are now in position: ", pos)
            row = pos // 5
            col = pos % 5
            lst[row][col] = name

            for ele in lst:
                print(ele)
    print("Game won")


main()
