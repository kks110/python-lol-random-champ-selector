import random
import setup_helper
import file_io


def setup():
    setup_helper.install_dependencies()
    file_io.create_champ_list()


def app():
    champs = file_io.champ_list_after_bans()
    champ_count = len(champs)
    player_count = input('How many players need champs picked for them?: ')
    champs_per_player = input('How many champs per player?: ')
    for player in range(int(player_count)):
        print('\nPlayer ' + str(int(player)+1) + ':')
        for champ in range(int(champs_per_player)):
            print(champs[random.randint(0, (champ_count-1))])


def main():
    setup()
    app()


if __name__ == "__main__":
    main()
