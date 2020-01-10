from tkinter import *
import file_io

root = Tk()
root.geometry('800x300')
frame = Frame(root)
frame.pack()


def button_settings(text_value):
    return {
        'text': text_value,
        'width': 30,
        'height': 5,
        'bd': 10,
    }


def to_ban_champ_screen():
    random_champs_button.pack_forget()
    ban_champ_button.pack_forget()
    ban_champ_screen_setup()


def ban_champ_screen_setup():
    champ_list = Listbox(root)
    counter = 1
    for champ in file_io.banned_champs():
        champ_list.insert(counter, champ)
        counter += 1
    champ_list.pack()




random_champs_button = Button(frame, button_settings('Random Champs'))
random_champs_button.pack(side=LEFT)

ban_champ_button = Button(frame, button_settings('Add champ to the ban list'), command=to_ban_champ_screen)
ban_champ_button.pack(side=LEFT)
root.mainloop()