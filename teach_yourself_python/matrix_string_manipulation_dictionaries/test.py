import sys

student_records = {"John Larson": 40, "Joe Bloggs": 21, "Hannah Marvin": 37}

def main():
    print("""
============WELCOME TO MAIN MENU================
    Please choose one:
    V - View all student's details (sorted by number of games won)
    A - Add a student to your records
    D - Delete a student from your records
    U - Update records (e.g.: increase the number of games each student has won)
    S - Search by student (and return the number of games won)
    Q - Quit the program
    """)
    choice = input("What are you going to do? >>> ")
    if choice == "V" or choice == "v":
        view_details()
    elif choice == "A" or choice == "a":
        add_student()
    elif choice == "D" or choice == "d":
        delete_student()
    elif choice == "U" or choice == "u":
        update_records()
    elif choice == "S" or choice == "s":
        search_student()
    elif choice == "Q" or choice == "q":
        sys.exit()
    else:
        print("Please make a valid choice")


def view_details():
    print("=========== View all student's details=================")
    if bool(student_records):
        sorted_record = sorted(student_records.items(), key= lambda i:i[1])
        for k, v in sorted_record:
            print(k, ":", v)
    else:
        print("There is no student records found")
    main()


def add_student():
    print("========== Add new student's records ==============")
    num_of_students = int(input("How many students' records you want to add? >>> "))
    print("You are adding", num_of_students, "students' records")
    for i in range(num_of_students):
        name = input("Enter student's name: ")
        num_of_games = int(input("Enter number of games won: "))
        student_records[name] = num_of_games
        print("")
    main()


def delete_student():
    print("========== Delete student's record ==============")
    name = input("Enter student's name you want to delete: ")
    if name.title() in student_records:
        del student_records[name.title()]
    else:
        print("Student's name not found")
    main()


def update_records():
    print("========== Update student's records ==============")
    name = input("Enter student's name you want to update: ")
    if name.title() in student_records:
        student_records[name.title()] = int(input("Enter new number of games won: "))
    else:
        print("Student's name not found")
    main()


def search_student():
    print("========== Search for student's records ==============")
    name = input("Enter student's name: ")
    if name.title() in student_records:
        print(name.title(), ":", student_records[name.title()])
    else:
        print("Student's name not found")
    main()


main()
