import validation_helpers
import file_io


def list_bans():
    banned_champs = file_io.banned_champs()
    all_champs = file_io.read_champs()
    print("\nThe current banned champs are:")
    for champ in banned_champs:
        if champ in all_champs:
            print(champ)
    print()


def ban_a_champ():
    print("If spelling isn't your strong point, there is a banned_champs.txt file")
    print("You can remove the # from in front of a champs name to ban them")
    banned_champs = file_io.banned_champs()
    while True:
        champ_to_ban = input("Who would you like to ban: ")
        champ_to_ban = champ_to_ban.lower().replace(" ", "")
        not_changed = True
        for champ in banned_champs:
            if champ.lower().replace(" ", "") == "#" + champ_to_ban:
                banned_champs.remove(champ)
                champ = champ[1:]
                print("Banned " + champ)
                banned_champs.append(champ)
                not_changed = False
        if not_changed:
            print("Could not find that champion to ban")
        another = input("Would you like to ban another? (Y/n): ")
        if another.lower() == "n":
            break
    file_io.save_bans(banned_champs)


def ban_menu():
    while True:
        print("Would you like to:")
        print("    1 - See currently banned champs?")
        print("    2 - Ban a champ?")
        print("    3 - Un-ban a champ")
        print("    4 - Return to main menu")
        choice = validation_helpers.multiple_choice_validation(2)
        if choice == 1:
            list_bans()
        elif choice == 2:
            ban_a_champ()
