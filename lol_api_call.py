import requests


def data_version():
    ddragon = "https://ddragon.leagueoflegends.com/realms/euw.json"
    euw_json = requests.get(ddragon).json()
    return euw_json['n']['champion']


def build_data_url():
    return "http://ddragon.leagueoflegends.com/cdn/" + data_version() + "/data/en_GB/champion.json"


def get_champs():
    champ_data = requests.get(build_data_url()).json()
    return list(champ_data['data'].keys())


def save_champs():
    champ_list = get_champs()
    file = open('champ_list.txt', 'w')
    for champ in champ_list:
        file.write(champ + "\n")


def saved_champ_count():
    return len(open('champ_list.txt').readlines())


def champion_count():
    return len(get_champs())
