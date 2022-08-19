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
        return '{}{}'.format(self.string,other)

    def substring(self,start,end):
        if start > end:
            return None

        substr = ''
        for i in range(start,end):
            if i >= self.length:
                break
            substr = MyString(substr)
            substr = substr.add_string(self.string[i])
        return substr

    def insert_string(self,pos,other):
        if pos > self.length:
            return "Position is exceed the length of string!"

        st_part = MyString.substring(self,0,pos)
        last_part = MyString.substring(self,pos,self.length)
        # ins_str =  st_part + other + last_part
        st_part = MyString(st_part)
        ins_str = MyString(st_part.add_string(other)).add_string(last_part)
        return ins_str

    def delete_string(self,start,end):
        if start > end:
            return self.string

        st_part = MyString.substring(self,0,start)
        last_part = MyString.substring(self,end,self.length)
        if last_part is None:
            return st_part

        # del_str = st_part + last_part
        st_part = MyString(st_part)
        del_str = st_part.add_string(last_part)
        return del_str

    def replace_string(self,start,end,other):
        if start > end:
            return self.string

        steps = end - start
        st_part = MyString.substring(self,0,start)
        last_part = MyString.substring(self,end,self.length)
        st_part = MyString(st_part)

        added_part = ''
        for i in range(0,steps):
            if start + i < self.length:
                added_part = MyString(added_part).add_string(other[i])

        if last_part is None:
            if st_part is None:
                return self.string
            return st_part.add_string(added_part)
        # r_str = st_part + added_part + last_part
        r_str = MyString(st_part.add_string(added_part)).add_string(last_part)
        return r_str

str1 = MyString('Hello Gemma!')

print(str1.len())
print(str1.add_string(' Nice to meet you.'))

print('---------------------------')
print(str1.substring(2,4))
print(str1.substring(0,1))          # get first char
print(str1.substring(4,1))          # start > end
print(str1.substring(4,18))         # end > length
print(str1.substring(16,18))        # start > length, end > length

print('---------------------------')
print(str1.insert_string(1,'!'))
print(str1.insert_string(0,'X'))
print(str1.insert_string(0,''))     # insert nothing
print(str1.insert_string(15,'Y'))   # exceed length

print('---------------------------')
print(str1.delete_string(0,2))
print(str1.delete_string(0,12))     # delete whole string
print(str1.delete_string(0,1))      # delete first char
print(str1.delete_string(11,12))    # delete last char
print(str1.delete_string(9,16))     # start < length, end > length
print(str1.delete_string(15,16))    # start > length, end > length

print('---------------------------')
print(str1.replace_string(0,2,'ABCD'))
print(str1.replace_string(1,3,'ABCD'))
print(str1.replace_string(11,12,'ABCD'))    # last char
print(str1.replace_string(9,16,'ABCD'))     # start < length, end > length
print(str1.replace_string(15,16,'ABCD'))    # start > length, end > length
print('---------------------------')
