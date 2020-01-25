
def player_count_validation():
    while True:
        player_count = input('How many players?: ')
        try:
            return int(player_count)
        except ValueError:
            print('Please enter a valid number of players')


def champion_count_validation():
    while True:
        champ_count = input('How many champs per player?: ')
        try:
            return int(champ_count)
        except ValueError:
            print('Please enter a valid number of champs')