# Task 1: area of rectangle
def rectangle_area():
    length = int(input("Enter length: "))
    breadth = int(input("Enter width: "))
    area = length * breadth
    print(f"Area of the rectangle with length is {length}, breadth is {breadth}: {area}")


# Task 2: user's information
def user_info():
    name = input("Hi there, what's your name: ")
    food = input(f"Nice to meet you, {name}. What is your favorite food: ")
    subject = input("Interesting! How about your favorite subject at school: ")
    print("This is your introduction:")
    print(f"My name is {name}, I love {food} and my favorite subject is obviously {subject}")


# Task 3: multiply numbers
def multiply():
    num = int(input("Enter your favorite number: "))
    print(f"{num} x 100 is equal to: {num*100}")

# Task 4: manage pocket money
def pocket_money():
    current = int("Enter your pocket money: ")
    spent = int("How much have you spent? ")
    left = current - spent
    print("Your amount left is:", left)

# Task 5: create a customised username
def username():
    birth = input("Please enter your last two numbers of date of birth (i.e. 1987 would be 87): ")
    last_name = input("What is your last name: ")
    print("Great! Your username should be: " + birth + last_name)

rectangle_area()
user_info()
multiply()
pocket_money()
username()
