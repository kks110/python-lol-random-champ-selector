

def match_builder(match_number, match_details):
    player_1 = match_details['player_1']
    player_2 = match_details['player_2']

    print('_________________________________________________')
    print('| Match %s:                                      |' % match_number)
    print('|-----------------------------------------------|')
    print('| Player: %s| Player: %s|' % (space_calc(player_1['name']), space_calc(player_2['name'])))
    if len(match_details['player_1']['champs']) != 0:
        print('| Champs: %s| Champs: %s|' % (space_calc(player_1['champs'][0]), space_calc(player_2['champs'][0])))
        for x in range(len(player_1['champs'])-1):
            champ_number = x + 1
            print('|         %s|         %s|' % (space_calc(player_1['champs'][champ_number]), space_calc(player_2['champs'][champ_number])))
    print('|_______________________|_______________________|')
    print()


def space_calc(name):
    white_space = 14 - len(name)
    spaces = white_space * " "
    cell = name + spaces
    return cell
