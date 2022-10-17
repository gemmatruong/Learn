# Write a Python program to calculate the value of "a" to the power "b"
def power(a, b):
    if b == 0:
        return 1
    else:
        result = 1
        if b < 0:
            if a != 0:
                for _ in range(b, 0):
                    result /= a
                return result
            return "Cannot calculate"
        else:
            for _ in range(1, b + 1):
                result *= a
            return result

print(power(2, 3))      # 8
print(power(5, 0))      # 1
print(power(5, 1))      # 5
print(power(5, -2))     # 0.04
print(power(0, 5))      # 0
print(power(100, 2))    # 10000
print(power(-5, 3))     # -125
print(power(-5, 4))     # 625
print(power(4, -2))     # 0.0625
print(power(0, 0))      # 1
print(power(0, -4))     # Cannot calculate

# Alternative way: using recursion. It cannot be used to deal with negative exponent
def power2(a, b):
	if b == 0:
		return 1
	elif a == 0:
		return 0
	elif b == 1:
		return a
	else:
		return a * power2(a, b-1)