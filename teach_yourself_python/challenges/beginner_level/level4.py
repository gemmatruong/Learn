# Task 1: print 6 characters of a string
def six_chars():
    s = input("Enter a string: ")
    print("{:.6s}".format(s))


# Task 2: odd or even number
def odd_or_even():
    try:
        num = int(input("Enter number: "))
        if num < 0:
            print("Please enter a natural number")
        else:
            if num % 2 == 0:
                print("Oood, that's an odd number!")
            else:
                print("Oooh, that's an even number!")
    except:
        print("Invalid input format")

# Task 3: check positive number
def check_number():
    num = int(input("Enter a number: "))
    if num < 0:
        print(f"{num} is a positive number")
    elif num > 0:
        print(f"{num} is a negative number")
    else:
        print("It is zero")

# Task 4: concatenation
def concatenation():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Hello " + last_name + " " + first_name)

# Task 5: remove numbers after decimal point
def remove_decimal():
    num = float(input("Enter a floating point/ decimal number and we'll get rid of the decimals for you: "))
    print("{} getting rid of decimal points is: {}".format(num, int(num)))


six_chars()
odd_or_even()
check_number()
concatenation()
remove_decimal()
