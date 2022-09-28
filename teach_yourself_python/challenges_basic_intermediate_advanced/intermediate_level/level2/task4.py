def sum_list(lst):
    result = 0
    for ele in lst:
        result += ele
    return result

try:
    lst = list(map(int, input("Enter a list of numbers: ").split()))
    if len(lst) == 0:
        print("Empty list")
    else:
        print(sum_list(lst))
except:
    print("Invalid input format")
