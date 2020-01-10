import os.path
import setup_helper
import lol_api_call


def setup():
    setup_helper.install_dependencies()


def create_champ_list():
    if not os.path.exists('champ_list.txt'):
        lol_api_call.save_champs()
        print('Downloading champion list...')
    if lol_api_call.champion_count() != lol_api_call.saved_champ_count():
        print('Looks like there are some new champs\nDownloading...')
        lol_api_call.save_champs()
    print('Download complete!')



def main():
    setup()
    create_champ_list()
    input()

if __name__ == "__main__":
    main()