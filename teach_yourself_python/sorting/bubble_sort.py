def bubble_sorting(lst):
    # Let i varies from the last index to the first index
    for i in range(len(lst)-1, 0, -1):
        # Let j varies from the first index to i. Buble sort makes the biggest number go to the end of list
        for j in range(i):
            if lst[j] > lst[j+1]:
                # Swap position of two adjacent elements
                lst[j], lst[j+1] = lst[j+1] , lst[j]

lst = [18, 9, 58, 6, 43, 0]
bubble_sorting(lst)
print("Sorted list is:", lst)
