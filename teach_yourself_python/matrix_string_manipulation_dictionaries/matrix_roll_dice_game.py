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
    lst = matrix_list()
    for ele in lst:
        print(ele)
    
    name = input("Enter a letter that will be your player name: ")
    print("Thank you", name)
    num = int(input("Please enter a number from 1 to 5: "))
    print("Well done, " + name + "! You are now in position: ", num)
    lst[0][num] = name

    for ele in lst:
        print(ele)


main()
