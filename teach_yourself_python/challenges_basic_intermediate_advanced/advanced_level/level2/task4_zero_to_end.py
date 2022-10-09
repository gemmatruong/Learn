# Write a Python program to push all zeros to the end of a list
def zero_to_end(lst):
    if len(lst) == 0:
        return "Empty list"
    else:
        for i in range(len(lst)):
            if lst[i] == 0:
                lst.remove(lst[i])
                lst += [0]
        return lst

lst1 = [7, 10, 0, 9, 11, 0, 17]
lst2 = [1, 2, 3, 4, 5, 6, 7]
lst3 = [0, 0, 0, 0, 0, 0, 0, 1]
lst4 = []
lst5 = [0, 0, 0, 0]

print(zero_to_end(lst1))    # [7, 10, 9, 11, 17, 0, 0]
print(zero_to_end(lst2))    # [1, 2, 3, 4, 5, 6, 7]
print(zero_to_end(lst3))    # [1, 0, 0, 0, 0, 0, 0, 0]
print(zero_to_end(lst4))    # Empty list
