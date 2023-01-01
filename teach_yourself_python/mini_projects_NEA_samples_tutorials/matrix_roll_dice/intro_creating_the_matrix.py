def main():
    print("~~~~~~~~~~~~~~~~ ROLL DICE ~~~~~~~~~~~~~~~~")
    print_matrix(7)



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

main()
