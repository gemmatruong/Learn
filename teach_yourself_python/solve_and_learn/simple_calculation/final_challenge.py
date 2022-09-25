def cal_speed():
    print(">>> Calculate your speed here <<<")
    distance = int(input("Enter a distance in meter: "))
    time = int(input("How long did it take you to finish running (should be in second): "))
    speed = round(distance/time,2)
    print("Your speed is", speed, "seconds per meter.")


cal_speed()