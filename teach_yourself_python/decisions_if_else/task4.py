def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "hello" and password == "open123":
        print("Access Granted")
        secret_code()
    else:
        print("Access Denied")

def secret_code():
    code = input("What's the secret code? >>> ")
    if code == "7777":
        print("Welcome AGENT")
    else:
        print("Wrong code. Try again")
        secret_code()

     
login()