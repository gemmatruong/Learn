class friend_of_Gemma:
    height = 160
    def __init__(self, para_name, para_age, para_charc):
        self.name = para_name
        self.age = para_age
        self.characteristic = para_charc
    

# class best_friend(friend_of_Gemma):
#     height = 170
#     def __init__(self, para_name,para_age,para_charc,para_skill):
#         self.name = para_name
#         self.age = para_age
#         self.characteristic = para_charc
#         #add new attribute:
#         self.skill = para_skill

#another way to create a child class:
class best_friend(friend_of_Gemma):
    height = 180
    def __init__(self, para_name,para_age,para_charc,para_skill):
        super().__init__(para_name, para_age, para_charc)
        self.skill = para_skill

firstBestFriend = best_friend('Thuy Linh', 23, 'smart', 'audit')
print(firstBestFriend.__dict__)
print(firstBestFriend.skill)
