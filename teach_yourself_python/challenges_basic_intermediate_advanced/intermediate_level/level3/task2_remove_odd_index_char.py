def remove_char(s):
    new_s = ""
    for i in range(len(s)):
        if i % 2 == 0:
            new_s += s[i]
    return new_s

s = input("Enter a string: ")
print("The string after removing the characters which has odd index is:", remove_char(s))
