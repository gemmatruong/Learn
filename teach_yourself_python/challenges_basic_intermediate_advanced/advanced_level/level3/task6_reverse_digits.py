# Write a Python program to reverse the digits of an integer

def reverse_digits(num):
    temp = num
    if temp < 0:
        temp = temp * -1
    
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp = temp // 10
    
    if num < 0:
        reversed_num = reversed_num * -1
    return reversed_num

print(reverse_digits(0))         # 0
print(reverse_digits(234))       # 432
print(reverse_digits(-234))      # -432
print(reverse_digits(11))        # 11
print(reverse_digits(12345678))  # 87654321
