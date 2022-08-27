import time

def verify():
    print("===CHECKING IDENTITY=====")
    time.sleep(1.1)
    print(".....please wait while we do important stuff....")
    time.sleep(1.1)
    print("-----Are you Ready----?")
    name = input("Enter the secret password: ")
    if name == "Joe":
        print("Access Granted")
    else:
        print("Access Denied")
        verify()

verify()