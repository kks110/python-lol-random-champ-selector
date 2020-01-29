import validation_helpers


def main_menu():
    print("Welcome to the League of Legends Tournament manager")
    print("Would you like to:")
    print("    1 - Create a tournament?")
    print("    2 - Check the ban situation")
    choice = validation_helpers.main_menu_validation()
    if choice == 1:
        return "bracket"
    else:
        return "bans"
