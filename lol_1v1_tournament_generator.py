import setup_helper
import file_io
import bracket_generator
import gui_generator
import validation_helpers


def setup():
    setup_helper.install_dependencies()
    file_io.create_champ_list()


def app():
    player_count = validation_helpers.player_count_validation()
    champ_count = validation_helpers.champion_count_validation()

    bracket_generator.get_players(player_count, champ_count)
    bracket = file_io.load_bracket()
    while len(bracket) > 0:
        counter = 1
        for x in range(len(bracket)):
            gui_generator.match_builder(int(x) + 1, bracket['match_%s' % counter])
            counter += 1
        print('Good Luck summoners\n\n')
        bracket_generator.round_complete(bracket, champ_count)
        bracket = file_io.load_bracket()


def main():
    setup()
    app()


if __name__ == "__main__":
    main()
