import re

def password_validation():
    valid = False
    while valid is False:
        password = input("Enter password: ")
        if 6 <= len(password) <= 16:
            if re.search("[A-Z]", password):
                if re.search("[a-z]", password):
                    if re.search("[0-9]", password):
                        if re.search("[$#@]", password):
                            print("Successful password. Congratulations")
                            valid = True
                        else:
                            print("Your password must contain at least one special character such as $, # or @")
                    else:
                        print("Your password must contain at least one number")
                else:
                    print("Your password must contain at least one regular alphabet")
            else:
                print("Your password must contain at least one capital character")
        else:
            print("Length of password must be between 6 and 16 characters")

password_validation()