# Write a program to find 3 elements that sum to zero from a list of n real numbers
# Algorithm 1: create by me
def sum_to_zero(lst):
    lst = sorted(lst)
    zero_sum_list = []
    for i in range(len(lst)-2):
        first_num = lst[i]
        for j in range(i+1, len(lst)-1):
            second_num = lst[j]
            k = j + 1
            find_out = False
            while find_out is False and k < len(lst):
                third_num = lst[k]
                if first_num + second_num + third_num == 0:
                    if [first_num, second_num, third_num] not in zero_sum_list:
                        zero_sum_list.append([first_num, second_num, third_num])
                    find_out = True
                else:
                    k += 1
    return zero_sum_list

print(sum_to_zero([-25, -10, -5, -3, -7, -3, -2, 4, 8, 10, 25, 0]))


# Algorithm 2: Learn from w3resoure.com. I think it is more time-saving
def three_sum(nums):
    nums = sorted(nums)
    result = []
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] < 0:
                j += 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j, k = j + 1, k - 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
        i += 1
        while i < len(nums) - 2 and nums[i] == nums[i - 1]:
            i += 1
    return result

print(three_sum([-25, -10, -5, -3, -7, -3, -2, 4, 8, 10, 25, 0]))
