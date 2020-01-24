import setup_helper
import file_io
import random_champ_generator


def setup():
    setup_helper.install_dependencies()
    file_io.create_champ_list()


def app():
    while True:
        player_count = input('How many players need champs picked for them?: ')
        champs_per_player = input('How many champs per player?: ')
        for player in range(int(player_count)):
            print('\nPlayer ' + str(int(player)+1) + ':')
            print(random_champ_generator.generate_champs(int(champs_per_player)))

        loop = input('\nWould you like to get more random champs? (Y/n): ')
        if loop.lower() == 'n':
            break


def main():
    setup()
    app()


if __name__ == "__main__":
    main()
