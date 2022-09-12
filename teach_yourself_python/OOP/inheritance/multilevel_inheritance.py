class Student:
    def __init__(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.gender = input("Gender: ")
    def printStudent(self):
        print("==========Printing Student Details========")
        print(self.name)
        print(self.age)
        print(self.gender)

class ComputingStudent(Student):
    def __init__(self):
        super(ComputingStudent, self).__init__()
        print("Enter the marks for your first three tests:")
        self.test1= int(input("Test1: "))
        self.test2 = int(input("Test2: "))
        self.test3 = int(input("Test3: "))

    def get_marks(self):
        print("=======PRINTING YOUR TEST SCORES====")
        print(self.test1)
        print(self.test2)
        print(self.test3)
        

class TopComputingStudent(ComputingStudent):
    def __init__(self):
        super(TopComputingStudent, self).__init__()
        self.total_marks = self.test1 + self.test2 + self.test3

    def display(self):
        print("\n\nName: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

        print("Total Marks: ", self.test1 + self.test2 + self.test3)

    def eligible_for_reward(self):
        print("===== TRIP TO LONDON ====")
        if self.age > 13 and self.total_marks > 90:
            print("You are eligible for the reward trip to London!")
        else:
            print("Sory, you are not eligible")


if __name__ == "__main__":
    s2 = TopComputingStudent()
    s2.printStudent()
    s2.get_marks()
    s2.eligible_for_reward()

    s1 = TopComputingStudent()
    s1.display()
    s1.eligible_for_reward()
