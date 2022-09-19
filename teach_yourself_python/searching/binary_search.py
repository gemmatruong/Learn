def binary_search(friend, list_of_friends):
    first = 0
    last = len(list_of_friends) - 1

    while last >= first:
        mid = (first + last) // 2

        if list_of_friends[mid] == friend:
            print("Found in  position", mid)
            break
        else:
            if friend < list_of_friends[mid]:
                last = mid - 1
            else:
                first = mid + 1
    else:
        print("Not found")


list_of_friends = ["Albert", "Andy", "Bob", "Ed", "Gemma"]
friend = input("Enter a name: ")
binary_search(friend, list_of_friends)
