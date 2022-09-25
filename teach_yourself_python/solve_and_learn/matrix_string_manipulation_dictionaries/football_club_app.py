import sys

players_dict = dict()

def main():
    print("""
================ MAIN MENU ================
    1----Add players
    2----Search players (return average)
    3----Update Goals for players
    4----View all players
    5----Quit

    """)
    choice = input("Enter choice: ")
    if choice == "1":
        add_players()
    elif choice == "2":
        search_players()
    elif choice == "3":
        update_goals()
    elif choice == "4":
        view_all_players()
    elif choice == "5":
        sys.exit()
    else:
        print("Please enter valid choice")


def add_players():
    num_of_players = int(input("Please enter number of players you wish to enter: "))
    print("You are entering", num_of_players, "players")
    for player in range(num_of_players):
        name = input("Enter player's name: ")
        goals_dict = dict()
        goals_dict["Match 1 goals"] = int(input("Match 1 goals: "))
        goals_dict["Match 2 goals"] = int(input("Match 2 goals: "))
        goals_dict["Match 3 goals"] = int(input("Match 3 goals: "))
        
        players_dict[name] = goals_dict
        print("")
    main()


def search_players():
    print("============SEARCH by player: Calculate average goals===============")
    if bool(players_dict) is False:
        print("You have no players registed")
    else:
        name = input("Player name: ")
        if name in players_dict:
            print(sum(list(players_dict[name].values()))/3)
        else:
            print("Player name does not exist")
    main()


def update_goals():
    name = input("Which player's goals do you wish to update? ")
    if name in players_dict:
        m1 = int(input("Match 1 new entry: "))
        m2 = int(input("Match 2 new entry: "))
        m3 = int(input("Match 3 new entry: "))
        players_dict[name] = {"Match 1 goals": m1, "Match 2 goals": m2, "Match 3 goals": m3}
    else:
        print("Player does not exist")
    main()


def view_all_players():
    for player, infor in players_dict.items():
        print("{} - {}".format(player, infor))
    main()

main()
