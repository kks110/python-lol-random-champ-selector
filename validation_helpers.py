
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


def multiple_choice_validation(choice_count):
    while True:
        bracket_or_ban = input("(Please enter a number between 1 and %s): " % str(choice_count))
        try:
            choice = int(bracket_or_ban)
            if 0 < choice <= choice_count:
                return choice
        except ValueError:
            print("Choice must be a number between 1 and %s" % choice_count)
