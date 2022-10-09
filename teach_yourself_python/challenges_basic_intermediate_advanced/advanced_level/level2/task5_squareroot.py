# Write a Python program to compute and return the square root of an given integer
# Note: returned value will be an integer
def squareroot(num):
    if num < 0:
        return "Squareroot cannot be negative"
    elif num == 1:
        return 1
    else:
        for i in range(0, num//2 + 1):
            if i*i == num:
                return i
        return None

num1 = 1
num2 = 2
num3 = 4
num4 = 8
num5 = 16
num6 = 17
num7 = 100
num8 = 0
num9 = -4

print(squareroot(num1))     # 1
print(squareroot(num2))     # None
print(squareroot(num3))     # 2
print(squareroot(num4))     # None
print(squareroot(num5))     # 4
print(squareroot(num6))     # None
print(squareroot(num7))     # 10
print(squareroot(num8))     # 0
print(squareroot(num9))     # Squareroot cannot be negative
