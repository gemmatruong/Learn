# Write a Python program to check if a given string is an anagram of another given string
def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        i = 0
        while i < len(s1):
            if s1[i] not in s2:
                return False
            i += 1
        return True

s1 = "anagram"
s2 = "nagaram"
print(check_anagram(s1, s2))    # True

s3 = "Hello"
s4 = "elloh"
print(check_anagram(s3, s4))    # False

s5 = "~~~~~~~~e"
s6 = "!!e"
print(check_anagram(s5, s6))    # False
