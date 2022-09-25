def quick_sort(lst):
   quick_sort_hlp(lst, 0, len(lst)-1)

def quick_sort_hlp(lst, first, last):
   if first < last:

       split_point = partition(lst, first, last)

       quick_sort_hlp(lst, first, split_point-1)
       quick_sort_hlp(lst, split_point+1, last)


def partition(lst, first, last):
   pivot = lst[first]

   left_mark = first + 1
   right_mark = last

   done = False
   while not done:

       while left_mark <= right_mark and lst[left_mark] <= pivot:
           left_mark = left_mark + 1

       while lst[right_mark] >= pivot and right_mark >= left_mark:
           right_mark = right_mark - 1

       if right_mark < left_mark:
           done = True
       else:
           temp = lst[left_mark]
           lst[left_mark] = lst[right_mark]
           lst[right_mark] = temp

   temp = lst[first]
   lst[first] = lst[right_mark]
   lst[right_mark] = temp


   return right_mark

lst = [18, 9, 58, 6, 43, 0]
quick_sort(lst)
print(lst)


# This is an easier way to understand about quick_sort
# But this function do not modify the existed list, it creates a new one
# def quick_sort(lst):
#     if len(lst) > 1:
#         pivot = lst.pop()
#     else:
#         return lst
    
#     items_greater = []
#     items_lower = []

#     for item in lst:
#         if item > pivot:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


# lst = [18, 9, 58, 6, 43, 0]
# print(quick_sort(lst))