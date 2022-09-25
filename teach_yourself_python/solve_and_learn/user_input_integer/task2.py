def simple_calc():
    #add another variable and ask for a number input for 'z'
    #make the total variable add up the three numbers x+y+z
    x = input("Enter a number: ")
    y = input("Enter the second number: ")
    z = input("Enter the third number: ")
    total = int(x) + int(y) + int(z)
    print("Adding these numbers will give you", total)


simple_calc()