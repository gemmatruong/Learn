# Method 1: using for loop
def factorial_m1(num):
    if num < 0:
        return "Invalid input"
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

print(factorial_m1(0))     # 1
print(factorial_m1(1))     # 1
print(factorial_m1(10))    # 3628800
print(factorial_m1(13))    # 6227020800
print(factorial_m1(-1))    # Invalid input

# Method 2: using recursion
def factorial_m2(num):
    if num < 0:
        return "Invalid input"
    elif num == 0:
        return 1
    else:
        return num * factorial_m2(num-1)

print(factorial_m2(0))     # 1
print(factorial_m2(1))     # 1
print(factorial_m2(10))    # 3628800
print(factorial_m2(13))    # 6227020800
print(factorial_m2(-1))    # Invalid input
