class String:      
    def reverse_string(self, s):
        words_list = s.split()
        words_list.reverse()
        return " ".join(words_list)

s = input("Enter a string: ")
print(String().reverse_string(s))
