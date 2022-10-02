# Write a Python program to calculate the sum of a list of numbers
def sum_of_list(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

lst = [0, -3, 4, 19, 27, -11, 0, 43]
# lst = int(input("Enter a list of number: "))
if len(lst) == 0:
    print("Empty list")
else:
    print(sum_of_list(lst))
