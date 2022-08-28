def main():
    print("*******************************WELCOME**************************************")
    name = (input("Hello there - what is your name? -"))
    print("What a lovely name ..." + name)
    birth = input("What is your date of birth e.g. April 22? -")
    print("Wow, I bet " + birth + " was a lovely day")
    country = input("I come from Vietnam. Where are you from? -")
    print("I know " + country + ", it is so beautiful.")
    food = input("Can you tell me about your favorite food? -")
    print(food + "is really nice, I have tried it before. A must-try dish")
    hobby = input("What do you like to do in your freetime? -")
    print("Such a healthy and balanced activity. Happy to hear that you love " + hobby)
    place = input("You know, you look gorguous today. Where did you buy your dress? -")
    print("It looks nice. I will come to see " + place + " when I have time.")
    weather = input("It's hot today, right? Do you know fahrenheit is it? -")
    print("OMG... no doubt why it's hot")
    movie_yes_no = input("Do you know Ozark series? It's my favorite movie. -")
    if movie_yes_no == 'yes':
        print("That's amazing, huh")
    else:
        print("You should watch it once. Worth your time. Trust me")
    
    movie = input("How about you? What is your favorite movie? -")
    print(movie + "is wonderfull. I couldn't stop laughing when I watched.")
    time = input("Oh, would you mind if I asked what time it is now? -")
    print("Oh no. I have to go. It's too late. Bye")


main() 