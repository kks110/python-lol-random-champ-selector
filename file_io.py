import os.path
import lol_api_call
import json


def save_champs():
    champ_list = lol_api_call.get_champs()
    file = open('champ_list.txt', 'w')
    for champ in champ_list:
        if champ == 'MonkeyKing':
            champ = 'Wukong'
        file.write(champ + "\n")


def create_ban_file():
    champ_list = lol_api_call.get_champs()
    file = open('banned_champs.txt', 'w')
    for champ in champ_list:
        if champ == 'MonkeyKing':
            champ = 'Wukong'
        file.write('#' + champ + "\n")


def read_champs():
    return [line.rstrip('\n') for line in open('champ_list.txt')]


def saved_champ_count():
    return len(open('champ_list.txt').readlines())


def create_champ_list():
    if not os.path.exists('champ_list.txt'):
        save_champs()
        print('Downloading champion list...')
    if not os.path.exists('banned_champs.txt'):
        create_ban_file()
        print('Creating Ban list template...')

    saved_champs_count = saved_champ_count()
    champ_list_count = lol_api_call.riot_champion_count()

    if champ_list_count != saved_champs_count:
        print('Looks like there are some new champs\nDownloading...')
        save_champs()
        update_ban = input('Update ban template? (This will overwrite any bans already set): (Y/n)')
        if update_ban.lower() != 'n':
            create_ban_file()
    print('Champion list download complete!')


def banned_champs():
    return [line.rstrip('\n') for line in open('banned_champs.txt')]


def champ_list_after_bans():
    all_champs = read_champs()
    for champ in banned_champs():
        if champ in all_champs:
            all_champs.remove(champ)
    return all_champs


def save_bracket(bracket):
    with open('bracket.json', 'w') as json_file:
        json.dump(bracket, json_file)


def load_bracket():
    with open('bracket.json') as json_file:
        return json.load(json_file)
