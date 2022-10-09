# Write a Python program to calculate the sum of the positive integers of n + (n-2) + (n-4)...

def sum_series(n):
    if n < 0:
        return "n cannot be negative"
    x = 0
    sum = 0
    while n - x >= 0:
        sum += n - x
        x += 2
    return sum

print(sum_series(6))    # 12
print(sum_series(10))   # 30
print(sum_series(0))    # 0
print(sum_series(1))    # 1
print(sum_series(15))   # 64
print(sum_series(-2))   # n cannot be negative
