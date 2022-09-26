def check_palindrome(s):
    reversed_s = s[::-1]
    if reversed_s == s:
        print("It is a palindrome string")
    else:
        print("It is not a palindrome string")

s = input("Enter a string: ")
check_palindrome(s)
