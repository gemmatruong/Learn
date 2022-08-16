class MyString:
    def __init__(self,s):
        self.string = s
    
    def __str__(self):
        return self.string

    def len(self):
        count = 0
        for char in self.string:
            count += 1
        return count

    def __add__(self, other):
        return self.string + other.string
    
    def substring(self,start,end,step):
        substr = ''
        for i in range(start,end,step):
            if i >= MyString.len(self):
                break
            substr = substr + self.string[i]
        return substr

str_1 = MyString('Hello Gemma!')
str_2 = MyString(' Nice to meet you.')

print(str_1.len())
print(str_1 + str_2)
print(str_1.substring(0,3,1))