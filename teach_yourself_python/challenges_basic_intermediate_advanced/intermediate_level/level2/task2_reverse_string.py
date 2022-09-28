# Reverse by slicing
def reverse_string(s):
    return s[::-1]

# Reverse by for loop
def reverse_by_for_loop(s):
    reverse_s = ""
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s

s = input("Enter a string: ")
print(reverse_string(s))
print(reverse_by_for_loop(s))
