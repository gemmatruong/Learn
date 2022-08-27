def username():
    print("====Enter details and we will generate a username for you=====")
    first_name = input("Enter first three letters of first name >>> ")
    last_name = input("Enter last name >>> ")
    age = input("Enter your age with two digits e.g. 16 >>> ")
    four_nums = input("Enter four random numbers >>> ")
    print("We suggest your username be: " + age + four_nums + last_name + first_name)


username()