class Student:
    def set_no_of_courses(self):
        self.number_of_courses = 3

    def display_no_of_courses(self):
        print(self.number_of_courses)


class AdvancedStudent(Student):
    def set_no_of_courses(self):
        self.number_of_courses = 5

    def reset_no_of_courses(self):
        super().set_no_of_courses() # once you call the super function, it will return the value from the base/parent class

student = Student()
student.set_no_of_courses()
print("Number of courses taken by the Student : ", end = "")
student.display_no_of_courses()

advanced_student = AdvancedStudent()
advanced_student.set_no_of_courses()
print("Number of courses taken by the Advanced Student : ", end = "")
advanced_student.display_no_of_courses()
print("Number of courses taken by the Advanced Student after reset (this uses the super function to call the method of the base class again): ", end="")
advanced_student.reset_no_of_courses()
advanced_student.display_no_of_courses()
