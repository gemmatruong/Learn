def friends_list():
    friends = int(input("Enter No. of Friends: "))
    print("Thank you, you have, ", friends," friends")
    remove = int(input("Enter No. of Friends you wish to remove: "))
    remaining = friends - remove
    print("You have this many friends remaining: ", remaining)
    add = int(input("Tell us how many friends you want to add more: "))
    remaining += add
    print("The remaining number of friends you have: ", remaining)
          

friends_list()