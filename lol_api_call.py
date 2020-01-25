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


def riot_champion_count():
    return len(get_champs())
