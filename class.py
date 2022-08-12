class friend_of_Gemma:
    def __init__(self, para_name, para_age, para_characteristic):
        self.name = para_name
        self.age = para_age
        self.characteristic = para_characteristic

    def say_hi (self):
        return "My name is {}. Nice to meet you!".format(self.name)

firstFriend = friend_of_Gemma('Quynh Huong',23,'fashionable')
print(firstFriend.name)
print(firstFriend.age)
print(firstFriend.characteristic)
print(firstFriend.say_hi())
print(friend_of_Gemma.say_hi(firstFriend))