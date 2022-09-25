# Task 1: boolean expressions
def pass_mark():
    math = int(input("What did you get in your math mark? >>> "))
    math_pass_mark = 35
    print("You passed math exam:", math >= math_pass_mark)

    biology = int(input("What did you get in your biology mark? >>> "))
    bio_pass_mark = 60
    print("You passed biology exam:", biology >= bio_pass_mark)

    if math > biology:
        print("You are a better mathematician than you are a biologist")
    elif math < biology:
        print("You are a better biologist than you are a mathematician")

# Task 2: which number is greater
def greater_num():
    no1 = int(input("Enter No.1: "))
    no2 = int(input("Enter No.2: "))
    if no1 > no2:
        greater = no1
    elif no1 < no2:
        greater = no2
    else:
        greater = no1
    print("The greater number is", greater)

# Task 3: students' score of Miss Moose
def grade_of_students():
    name = input("Enter student's name: ")
    mark = int(input(f"Enter mark of {name}: "))
    if mark < 0 or mark > 100:
        print("Invalid mark")
    else:
        if mark < 25:
            grade = "F"
        elif 25 <= mark < 45:
            grade = "E"
        elif 45 <= mark < 50:
            grade = "D"
        elif 50 <= mark < 60:
            grade = "C"
        elif 60 <= mark < 80:
            grade = "B"
        else:
            grade = "A"
        print(f"{name}'s grade is {grade}")
grade_of_students()