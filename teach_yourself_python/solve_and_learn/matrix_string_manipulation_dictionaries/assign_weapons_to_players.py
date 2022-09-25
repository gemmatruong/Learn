def main():
    players = ["Player1", "Player2", "Player3", "Player4"]
    weapons = ["SWORD", "BELT OF TRUTH", "ARMOUR", "SHIELD OF FAITH"]
    for p, w in zip(players, weapons):
        print("{} has been assigned the: {}".format(p, w))


main()
