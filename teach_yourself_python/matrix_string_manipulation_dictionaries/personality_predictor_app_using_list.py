def main():
    print("***** THE PERSONALITY PREDICTOR! **********")
    name = input("....First, type in your name: >>> ")
    subject = input("OK, " + name + " What is/was your favorite subject in school? >>> ")
    hobby = input("Name one activity that you usually do in your freetime >>> ")
    app(name, subject, hobby)

    # subject_list = ["math", "music", "arts", "physics", "chemistry", "literature",
    # "history", "PE", "computing"]

    # hobby_list = ["watch movies", "play video game", "read", "hang out with friends",
    # "play sports", "listen to music", "hike, garden or camp", "draw and paint", "solve quizzes"]

def app(name, subject, hobby):
    print("======== YOUR PERSONALITY REVEALED ==========")
    if subject in ["math", "physics", "chemisty"]:
        print(name + """! Well, you are quite logical in thinking. You always know how to find
exactly the answer of your answer. You love something relating to science that is
so interesting...""", end = ". ")
    elif subject == "computing":
        print(name + """! Well, your personality tends to expose with technology and modern
device. You maybe want to study and work in high-tech environment, which shows you are so
cool in adapting new advanced stuff...""", end = ". ")
    elif subject in ["literature", "history"]:
        print(name + """! Well, linguistic intertelligence is the best words to describe your
personality. You familirize with words, poetry, books, etc. You also love researching about
culture and customs during the time...""", end = ". ")
    elif subject == "PE":
        print(name + """! Well, your muscle is always ready, right? You are kind of productive
person. You love doing physical activities that means you will really enjoy in a active and
energetic environment...""", end = ". ")
    else:
        print(name + """! Well, you don't need to do much but you're shining in your own way.
Everyone loves to be your friend because of your energy and unique personality. Maybe don't
recognize how bad people admire you...""", end = ". ")

    if hobby in ["watch movies", "listen to music", "draw and paint"]:
        print("""I bet you are fond of artistic field. It shows how interested you are. You love
drama, beauty and chilling scene, too...""")
    elif hobby in ["read", "play video game"]:
        print("""It's wonderful to stay alone in your own bed, right? You know many things and
keep trying to learn more and more. Even it's sometimes hard for you to get outside and do some
physical activities. But make sure your health are doing well.""")
    elif hobby in ["play sports", "hike, garden or camp"]:
        print("""So fascinating are you. You are a nice traveller. You have strength and knowledge.
That's why many friends consider you as a mentor when travelling""")
    elif hobby == "solve quizzes":
        print("""Everything around you must be working in a logical and strategic way. Someone
who has clear and critical views will easily attract you...""")
    else:
        print("""Ah.. You are kind of person who is afraid of being alone. Friendship is an
important factor of your life. And of course, you are also a good friend.""")


main()
