def strip_chars(s, chars_set):
    # new_s = ""
    # for c in s:
    #     if c not in chars_set:
    #         new_s += c
    # return new_s
    return "".join(c for c in s if c not in chars_set)

s = input("Enter a string: ")
chars_set = set(input("Enter list of chars that you want to strip: ").split(","))
print("The string after stripped is:", strip_chars(s, chars_set))
