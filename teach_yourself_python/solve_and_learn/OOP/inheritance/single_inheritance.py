class Course:
    name = "Python Course"
    contact_website = "www.teachyourselfpython.com"
    ho_location = "Caterham, United Kingdom"

    def contact_details(self):
        print("To contact us, simply go to", self.contact_website)

    def head_office_location(self):
        print("The head office location is in", self.ho_location)


class OOPCourse(Course):
    def __init__(self):
        self.description = "Course on OOP Fundamentals"
        self.trainer = "Mrs TeachYourselfPython herself"
        self.ho_location = "Caterham, United Kingdom"
        self.id = "#0023013"

    def trainer_details(self):
        print("This Course is about:",self.description, "and is run by:", self.trainer)

    def id_number(self):
        print("The ID number of this Course is", self.id)


course1 = OOPCourse()

course1.contact_details()
course1.trainer_details()

course2 = OOPCourse()

course2.head_office_location()
course2.id_number()
