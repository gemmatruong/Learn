def pocket_money():
    print("Check your piggy account....")
    current = int(input("How much money do you have in the piggy bank? >>> "))
    spent = int(input("How much money did you spend? >>> "))
    left = current - spent
    print("The money left you have: ", left)
    gift = int(input("How much money do you have as a gift? >>> "))
    left += gift
    print("Now, the money left you have: ", left)


pocket_money()