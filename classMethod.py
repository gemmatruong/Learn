class friend_of_Gemma:
    height = 160
    def __init__(self, para_name, para_age, para_characteristic):
        self.name = para_name
        self.age = para_age
        self.characteristic = para_characteristic
    
    #Update attribute height:
    # @classmethod
    # def update_height(cls,para_height):
    #     cls.height = para_height

    @classmethod #Create with input as a string s.
    def from_string(cls,s):
        lst = s.split('-')
        newLst = [ele.strip() for ele in lst]
        name, age, characteristic = newLst
        return cls(name,age,characteristic)

firstFriend = friend_of_Gemma('Quynh Huong',23,'fashionable')

s = 'Hue Chi-23-kind'
secondFriend = friend_of_Gemma.from_string(s)
print(secondFriend.name)
print(secondFriend.age)


