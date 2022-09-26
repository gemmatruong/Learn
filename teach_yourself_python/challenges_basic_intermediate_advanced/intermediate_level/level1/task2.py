def main():
    for col in range(1, 10):
        if col <= 5:
            for row in range(1, col + 1):
                print("*", end = "")
            print("")
        else:
            for row in range(1, 10 - col + 1):
                print("*", end = "")
            print("")

main()