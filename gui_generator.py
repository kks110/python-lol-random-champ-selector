

def match_builder(match_number, match_details):
    print('_________________________________________________')
    print('| Match %s:                                      |' % match_number)
    print('|-----------------------------------------------|')
    print('| Player: %s| Player: %s|' % (space_calc(match_details['player_1']['name']), space_calc(match_details['player_2']['name'])))
    print('| Champs: %s| Champs: %s|' % (space_calc(match_details['player_1']['champs'][0]), space_calc(match_details['player_2']['champs'][0])))
    if len(match_details['player_1']['champs']) > 1:
        for x in range(len(match_details['player_1']['champs'])-1):
            print('|         %s|         %s|' % (space_calc(match_details['player_1']['champs'][int(x)+1]), space_calc(match_details['player_2']['champs'][int(x)+1])))
    print('|_______________________|_______________________|')
    print()


def space_calc(name):
    name_length = len(name)
    white_space = 14 - name_length
    spaces = white_space * " "
    cell = name + spaces
    return cell
