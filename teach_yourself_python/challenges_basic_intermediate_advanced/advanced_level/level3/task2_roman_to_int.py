# Write a Python program to convert a roman numeral to an integer

def integer_convert(roman):
    roman_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    int_val = 0

    for i in range(len(roman)-1, -1, -1):
        temp = roman_val[roman[i]]
        # If we use temp, 2*temp in this condition, it's not work with thousand unit (e.g.MMMI)
        # We can only use 3*temp or 4*temp
        if 2*temp < int_val:
            int_val = int_val - temp
        else:
            int_val += temp
    return int_val


print(integer_convert("LVIII"))         # 58
print(integer_convert("III"))           # 3
print(integer_convert("XIV"))           # 14
print(integer_convert("CMIX"))          # 909
print(integer_convert("MCMXCIV"))       # 1994
print(integer_convert("I"))             # 1
print(integer_convert("MMMCMXCIX"))     # 3999
print(integer_convert("XXX"))           # 30
print(integer_convert("CCC"))           # 300
print(integer_convert("MMMI"))          # 3001



# References from Geeksforgeeks
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
 
def romanToDecimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        # Getting value of symbol s[i]
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res
