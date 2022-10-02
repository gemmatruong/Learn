def fibonacci(num):
    if num < 1:
        return "Invalid input"
    elif num <= 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(0))     # Invalid input
print(fibonacci(1))     # 1
print(fibonacci(2))     # 1
print(fibonacci(5))     # 5
print(fibonacci(11))    # 89
print(fibonacci(12))    # 144
print(fibonacci(13))    # 233
print(fibonacci(-1))    # Invalid input
