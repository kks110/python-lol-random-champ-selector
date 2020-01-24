import random
import file_io


def generate_champs(number_of_champs):
    champs = file_io.champ_list_after_bans()
    champ_count = len(champs)
    champ_array = []
    for champ in range(number_of_champs):
        champ_array.append(champs[random.randint(0, (champ_count - 1))])
    return champ_array