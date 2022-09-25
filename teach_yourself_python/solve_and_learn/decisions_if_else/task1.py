def secretcode():
    code = input("Enter your four digit secret code: ")
    if code == "7777":
        print("Access Granted, Welcome AGENT")
    elif code == "7776" or code == "7778":
        print("Close, but not quite")
    else:
        print("SECURITY ALERT!!!!! IMPOSTOR")


secretcode()