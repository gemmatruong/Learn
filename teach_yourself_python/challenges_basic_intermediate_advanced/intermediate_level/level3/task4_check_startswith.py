def starts_with(s, specified_chars):
    i = 0
    while i < len(specified_chars):
        if specified_chars[i] != s[i]:
            return False
        i += 1
    return True

s = input("Enter a string: ")
specified_chars = input("Starts with? ")
print(starts_with(s, specified_chars))
