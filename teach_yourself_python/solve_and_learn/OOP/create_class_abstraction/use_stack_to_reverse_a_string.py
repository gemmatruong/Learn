class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def report(self):
        return self.items

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False


word = input("Enter a word: ")

s = Stack()
r = ""
for i in word:
    s.push(i)

while s.isEmpty() == False:
    r += s.pop()
print("Reversed word is:", r)
