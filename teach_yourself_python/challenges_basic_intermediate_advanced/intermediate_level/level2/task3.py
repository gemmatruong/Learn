def multiply_elements(lst):
    result = 1
    for ele in lst:
        result *= ele
    return result
try:
    lst = list(map(float, input("Enter a list of numbers: ").rstrip().split()))
    if len(lst) == 0:
        print("Empty list")
    else:
        print(multiply_elements(lst))
except:
    print("Invalid input format")
