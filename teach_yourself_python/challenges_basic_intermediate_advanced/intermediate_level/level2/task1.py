def median():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    lst = [num1, num2, num3]
    lst.sort()
    print("The median is:", lst[1])

median()
