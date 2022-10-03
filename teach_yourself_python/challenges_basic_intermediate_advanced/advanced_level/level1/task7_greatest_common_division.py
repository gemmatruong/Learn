# Method 1: using for loop
def greatest_common_division(a, b):
    if a == 0 or b == 0:
        return ZeroDivisionError
    else:
        small = min(a, b)
        gcd_list = []
        for i in range(1, small + 1):
            if a % i == 0 and b % i == 0:
                gcd_list.append(i)
        return gcd_list[len(gcd_list) - 1]


print(greatest_common_division(1, 4))       # 1
print(greatest_common_division(4, 16))      # 4
print(greatest_common_division(28, 35))     # 7
print(greatest_common_division(15, 27))     # 3
print(greatest_common_division(7, 19))      # 1
print(greatest_common_division(0, 18))      # <class 'ZeroDivisionError'>


# Method 1: using recursion
def recur_gcd(a, b):
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return ZeroDivisionError
    elif low == 1:
        return 1
    else:
        return recur_gcd(low, high % low)

print(recur_gcd(1, 4))       # 1
print(recur_gcd(4, 16))      # 4
print(recur_gcd(28, 35))     # 7
print(recur_gcd(15, 27))     # 3
print(recur_gcd(7, 19))      # 1
print(recur_gcd(0, 18))      # <class 'ZeroDivisionError'>
