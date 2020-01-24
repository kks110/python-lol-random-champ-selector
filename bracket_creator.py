import random
import random_champ_generator
import file_io


def get_players():
    player_list = []
    while True:
        player = input('Please enter the players name: ')
        player_list.append(player)
        keep_going = input('Would you like to add another player? (Y/n): ')
        if keep_going == 'n':
            break
    player_bracket = create_bracket(player_list)
    file_io.save_bracket(player_bracket)


def create_bracket(player_list):
    if len(player_list) % 2 != 0:
        player_list.append('Bye')
    random.shuffle(player_list)
    match_count = len(player_list)-1
    bracket = {}

    for x in range(match_count):
        match = {
            'player_1': {
                'name': '',
                'champs': random_champ_generator.generate_champs(3)
            },
            'player_2': {
                'name': '',
                'champs': random_champ_generator.generate_champs(3)
            },
        }
        bracket['match_%s' % str(int(x)+1)] = match

    counter = 1
    while player_list:
        bracket['match_%s' % counter]['player_1']['name'] = player_list.pop(0)
        bracket['match_%s' % counter]['player_2']['name'] = player_list.pop(0)
        counter += 1
    return bracket


get_players()
