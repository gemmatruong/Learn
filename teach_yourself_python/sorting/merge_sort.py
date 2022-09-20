def merge_sort(lst):
    # If lst only has 1 element, no need to sort
    if len(lst) > 1:
        # Find the middle number and then split lst into two sublists
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Call merge_sort() function again to split each sublist into smaller sublists
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        # Use while loop to check if sublists do not run out of data
        while i < len(left_half) and j < len(right_half):
            # Compare elements from two sublist, if it is smaller, it should come first
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1      # With while loop, remember index increment
            else:
                lst[k] = right_half[j]
                j += 1      # With while loop, remember index increment
            k += 1      # With while loop, remember index increment

        # When one of two sublists runs out of data, append data from the other one to lst
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1
        
        while k < len(right_half):
            lst[k] = right_half[j]
            i += 1
            k += 1

lst = [18, 9, 58, 6, 43, 0]
merge_sort(lst)
print(lst)
