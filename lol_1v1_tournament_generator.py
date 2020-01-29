import setup_helper
import file_io
import bracket_generator
import gui_generator
import validation_helpers
import main_menu


def setup():
    setup_helper.install_dependencies()
    file_io.create_champ_list()



def app():
    start_point = main_menu.main_menu()

    if start_point == "bracket":
        player_count = validation_helpers.player_count_validation()
        champ_count = validation_helpers.champion_count_validation()

        bracket_generator.get_players(player_count, champ_count)
        bracket = file_io.load_bracket()
        while len(bracket) > 0:
            for number in range(len(bracket)):
                match_number = number + 1
                gui_generator.match_builder(match_number, bracket['match_%s' % match_number])
            print('Good Luck summoners\n\n')
            bracket_generator.round_complete(bracket, champ_count)
            bracket = file_io.load_bracket()


def main():
    setup()
    app()


if __name__ == "__main__":
    main()
