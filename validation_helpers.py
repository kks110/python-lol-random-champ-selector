
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


def main_menu_validation():
    while True:
        bracket_or_ban = input("(Please enter either 1 or 2): ")
        try:
            choice = int(bracket_or_ban)
            if 0 < choice <= 2:
                return choice
        except ValueError:
            print("Choice must be a number between 1 and 2")
