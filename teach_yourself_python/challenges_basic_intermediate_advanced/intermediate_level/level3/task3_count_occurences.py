def occurence_count(s):
    lst_of_words = s.split()
    set_of_words = set(lst_of_words)
    count_dict = dict()
    for word in set_of_words:
        count = lst_of_words.count(word)
        count_dict[word] = count
    return count_dict

s = input("Enter a sentence: ")
print(occurence_count(s))
