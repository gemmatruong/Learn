class Student:
    def __init__(self, name, test_score, attendance):
        self.name = name
        self.test_score = test_score
        self.attendance = attendance

    def has_achieved_target(self):
        if self.test_score >= 90:
            print("Target met, Well done!")
        else:
            print("Target not achieved")
    
    def model_student(self):
        if self.test_score >= 90 and self.attendance >= 90:
            print("Model student")
        else:
            print("Not quite a model student")


student1 = Student("Jonathan", 21, 90)
print(student1.name)
print(student1.test_score)
student1.has_achieved_target()
student1.model_student()
print("")
student2 = Student("Gemma", 95, 90)
print(student2.name)
print(student2.test_score)
student2.has_achieved_target()
student2.model_student()
