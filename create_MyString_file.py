class MyString:
    def __init__(self,s):
        self.string = s

    def len(self):
        count = 0
        for char in self.string:
            count += 1
        return count

    def add_string(self, new_str):
        return "{}{}".format(self.string, new_str)




str_1 = MyString('Hello my world!')

print(str_1.len())
print(str_1.add_string(' Loving you'))
