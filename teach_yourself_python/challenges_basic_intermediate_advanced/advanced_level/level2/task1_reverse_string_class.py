# Write a Python Class to reverse a string word by word
class Python:
    def __init__(self, s):
        self.string = s
    def reverse_words(self):
        words_list = self.string.split()
        words_list.reverse()
        return " ".join(words_list)

s1 = Python("Hello everyone! My name is Gemma")
s2 = Python("")
s3 = Python(" Hello o ~ ! k")
print(s1.reverse_words())   # Gemma is name My everyone! Hello
print(s2.reverse_words())   # Nothing
print(s3.reverse_words())   # k ! ~ o Hello
