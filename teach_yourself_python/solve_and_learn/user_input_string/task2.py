def chatbot():
    print("WELCOME TO THE CHATTERBOT")
    name = input("What is your name? ")
    print("Nice to meet you "+name)
    food = input("What is your favourite food, if you don't mind me asking: ")
    print(food+"...wow....mmm.....I quite like "+food+" too")
    favword = input("Tell me your favourite word and I'll repeat it five times, just because I can!: ")
    print(favword*5)
    movie = input("I also would like to know your favorite movie to know more about you: ")
    print("Interesting! That's a nice experience when watching " + movie +" with our friends.")
    subject = input("Now, how about your favorite subject at school? ")
    print("Amazing. I cannot handle " + subject + " when I was a student. Good job")


chatbot()