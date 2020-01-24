import random
import random_champ_generator
import file_io


def get_players(player_count, champ_count):
    player_list = []
    counter = 1
    for x in range(int(player_count)):
        player = input('Please enter player %s: ' % counter)
        player_list.append(player)
        counter += 1
    player_bracket = create_bracket(player_list, int(champ_count))
    file_io.save_bracket(player_bracket)


def round_complete(bracket, champ_count):
    player_list = []
    counter = 1
    if len(bracket) == 1:
        player_bracket = {}
        file_io.save_bracket(player_bracket)
        return
    for x in range(len(bracket)):
        game_winner = input('Who won game %s: ' % counter)
        player_list.append(game_winner)
        counter += 1
    player_bracket = create_bracket(player_list, int(champ_count))
    file_io.save_bracket(player_bracket)


def create_bracket(player_list, champ_count):
    if len(player_list) % 2 != 0:
        player_list.append('Bye')
    random.shuffle(player_list)
    bracket = {}

    counter = 1
    while player_list:
        match = {
            'player_1': {
                'name': player_list.pop(0),
                'champs': random_champ_generator.generate_champs(champ_count)
            },
            'player_2': {
                'name': player_list.pop(0),
                'champs': random_champ_generator.generate_champs(champ_count)
            },
        }
        bracket['match_%s' % str(counter)] = match
        counter += 1
    return bracket
