class MyString:
    def __init__(self,s):
        self.string = s
        self.length = MyString.len(self)

    def __str__(self):
        return self.string

    def len(self):
        count = 0
        for char in self.string:
            count += 1
        return count

    def add_string(self, other):
        return '{}{}'.format(self.string,other.string)

    def substring(self,start,end):
        substr = ''
        for i in range(start,end):
            if i >= self.length:
                break
            substr += self.string[i]
        return substr

    def insert_string(self,pos,other):
        st_part = MyString.substring(self,0,pos)
        last_part = MyString.substring(self,pos,self.length)
        ins_str =  st_part + other + last_part
        return ins_str

    def delete_string(self,start,end):
        st_part = MyString.substring(self,0,start)
        last_part = MyString.substring(self,end,self.length)
        del_str = st_part + last_part
        return del_str

    def replace_string(self,start,end,other):
        if start == 0:
            steps = end - start
        else:
            steps = end + 1 - start
        st_part = MyString.substring(self,0,start)
        last_part = MyString.substring(self,end,self.length)
        added_part = ''
        for i in range(0,steps):
            added_part += other[i]
        r_str = st_part + added_part + last_part
        return r_str


str1 = MyString('Hello Gemma!')
str2 = MyString(' Nice to meet you.')

print(str1.len())
print(str1.add_string(str2))
print(str1.substring(2,4))
print(str1.insert_string(1,'!'))
print(str1.delete_string(0,2))
print(str1.replace_string(0,2,'abcd'))
