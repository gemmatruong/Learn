class Dad:
    # Public attributes
    major = "coding"
    hobby = "travel"

    # Protected attributes
    _lastname = "Truong"
    _property = 'house'

    # Private attributes
    __banking_number = "0123456789"
    __facebook_password = "000000000"

class Daughter(Dad):
    def __init__(self, first_name):
        super(Daughter, self).__init__()
        self.first_name = first_name
    
    def show_hobbies(self):
        print("Her hobby can be", self.hobby)
    
    def show_lastname(self):
        print("Her last name is", self._lastname)

daughter1 = Daughter("Gemma")
daughter1.show_hobbies()
daughter1.show_lastname()
print(daughter1._lastname)

dad1 = Dad()
print(dad1._lastname)
print(dad1.__banking_number)
