class Person:  
    def __init__(self, person_name, person_age):  
        self.name = person_name  
        self.age = person_age

    def show_name(self):  
        print(self.name)  
  
    def show_age(self):  
        print(self.age)  


class Student:
    def __init__(self, student_id, subject):  
        self.student_id = student_id
        self.subject = subject
    def get_id(self):  
        return self.student_id
    def get_subject(self):
        return self.subject


class Enrolled(Person, Student):
    def __init__(self, name, age, student_id, subject, enrolled_date):  
        Person.__init__(self, name, age)  
        Student.__init__(self, student_id, subject)
        self.enrolled_date = enrolled_date

    def get_date(self):
        return self.enrolled_date


if __name__ == "__main__":
    enrolled1 = Enrolled('Joe Bloggs', 33, '001', "COMPUTING 101", "19/08/2022")
    
    enrolled1.show_name()
    print("ID No:", enrolled1.get_id())
    print("Date enrolled:", enrolled1.get_date())
    print("Subject:", enrolled1.get_subject())
