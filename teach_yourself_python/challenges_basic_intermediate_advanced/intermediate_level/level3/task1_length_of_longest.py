def longest_word(lst):
    max_length = len(lst[0])
    for word in lst:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

lst = input("Enter list of words separated by space: ").split()
if len(lst) == 0:
    print("Empty list")
else:
    print("Length of the longest word is:", longest_word(lst))
