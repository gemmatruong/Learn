def times_table():
    num = int(input("Enter a number: "))
    for i in range(21):
        result = num*i
        print("{} times: {} is equal to: {}".format(num, i, result))


times_table()
