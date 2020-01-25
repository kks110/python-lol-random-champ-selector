import random
import file_io


def generate_champs(champs_per_player):
    champ_array = []
    if champs_per_player == 0:
        return champ_array
    champs = file_io.champ_list_after_bans()
    champ_count = len(champs)
    for number in range(champs_per_player):
        while True:
            picked_champ = champs[random.randint(0, (champ_count - 1))]
            if picked_champ not in champ_array:
                champ_array.append(picked_champ)
                break
    return champ_array
