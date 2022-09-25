def insertion_sort(lst):
    # Let i varies from 1 to the end of list which is considered unsorted part
    for i in range(1, len(lst)):
        # assign element at i index to a variable call "compared_value"
        compared_value = lst[i]
        pos = i - 1

        # use while loop to find out the right position for "compared_value" in sorted part
        while pos >= 0 and lst[pos] > compared_value:
            lst[pos+1] = lst[pos]
            pos -= 1
        lst[pos+1] = compared_value

lst = [18, 9, 58, 6, 43, 0]
insertion_sort(lst)
print("Sorted list is:", lst)
