def linear_search(x, lst):
    for i in range(len(lst)):
        if lst[i] == x:
            print("Found in position", i)
            break
    else:
        print("Not found")


lst = [0, 1, 2, 3, 4, 6]
x = int(input("Enter a number: "))
linear_search(x, lst)