def secretcode2():
    print("======SECURITY PASS REQUIRED====")
    code = input("Enter your four digit secret code: ")
    if code == "7777" or code == "3333" or "2204" or "2402":
        print("Access Granted, Welcome AGENT")
    else:
        print("SECURITY ALERT!!!!! IMPOSTOR")

secretcode2()