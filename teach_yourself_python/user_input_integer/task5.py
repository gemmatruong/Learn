def division():
    global x, y
    x = int(input("Enter a number larger than 10: "))
    y = int(input("Enter a number between 1 and 5: "))
    z = x/y
    print("{} : {} = {}".format(x,y,z))
    multiply()

def multiply():
    m = x*y
    print("{} x {} = {}".format(x,y,m))


division()