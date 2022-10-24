# Write a Python class which has two methods get_string and print_string
# get_string accept a string from the user and print_string print the string in upper case

class MyString():
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")
    
    def print_string(self):
        print(self.string.upper())

s1 = MyString()
s1.get_string()
s1.print_string()