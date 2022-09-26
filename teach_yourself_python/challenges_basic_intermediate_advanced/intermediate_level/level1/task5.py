# Check whether an alphabet is vowal or consonant

import re

def check_vowel():
    char = input("Enter a letter: ")
    if len(char) == 1:
        if char.isalpha():
            if re.search("[ueoai]", char):
                print(f"{char} is a vowel")
            else:
                print(f"{char} is a consonant")

check_vowel()