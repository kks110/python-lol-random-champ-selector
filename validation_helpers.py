
def player_count_validation():
    while True:
        player_count = input('How many players?: ')
        try:
            int(player_count)
            return player_count
        except ValueError:
            print('Please enter a valid number of players')


def champion_count_validation():
    while True:
        champ_count = input('How many champs per player? (Minimum of 1): ')
        try:
            champ_count_int = int(champ_count)
            if champ_count_int <= 0:
                print('Please enter a number greater than 0')
            else:
                return champ_count
        except ValueError:
            print('Please enter a valid number of champs')