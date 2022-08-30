import time

def login():
    global fav_animal, fav_num, first_name
    print("""*********     Welcome to Sunflower Club    ***********

    Well... Let us know more about you......
    """)
    time.sleep(0.9)
    fav_num = input("What is your favorite number? >>> ")
    fav_animal = input("Nice number!\nWhat is your favorite animal? >>> ")
    first_name = input("Amazing!\nNow, enter your first name here >>> ")
    print("Waiting....")
    username = fav_num + first_name + fav_animal
    print("Your username is: " + username)
    time.sleep(1.1)
    print("Congratulations! Now, you are a member of Sunflower Club.")
    sunflower_club()

def sunflower_club():
    username = input("Enter your usesrname here >>> ")
    if username == fav_num + first_name + fav_animal:
        print("Well done, " + first_name + "! You can enjoy our funny activities right now")
    else:
        print("Wrong username. Try again")
        sunflower_club()


login()