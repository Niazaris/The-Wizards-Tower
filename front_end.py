import PySimpleGUI as sg
from main import Player
import enemies


def intro():
    intro_layout = [
        [sg.Text("WELCOME TO THE WIZARDS TOWER!", text_color="#37FD12")],
        [sg.Text("Enter name", text_color="black"), sg.Input(key="-INPUT-", text_color="black", size=(20, 1))],
        [sg.Button("ACCEPT"), sg.Button("EXIT")]
    ]

    intro_window = sg.Window("WIZARDS TOWER", intro_layout)

    while True:
        intro_event, intro_values = intro_window.read()
        if intro_event == sg.WINDOW_CLOSED or intro_event == "EXIT":
            break
        if intro_event == "ACCEPT":
            player_name = intro_values["-INPUT-"]
            intro_window.close()
            main(player_name)

def main(player_name):
    player = Player(player_name)
    button_labels = player.spell_book
    layout = [
        [sg.Text(player_name, text_color="WHITE")],
        [sg.Text(player.hp, text_color="RED"), sg.Text(player.mana, text_color="BLUE")],
        [sg.Button(image_filename='The-Wizards-Tower/red_dragon.jpg', image_size=(100, 40), border_width=0, key='-IMAGE_BUTTON-')],
        [sg.Button(button_label, key=f'-BUTTON-{index}-')
        for index, button_label in enumerate(button_labels)]
    ]
    window = sg.Window("WIZARDS TOWER", layout, size=(1024, 720))
    
   
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "EXIT GAME":
            window.close()
            break
        elif event.startswith('-BUTTON-'):
            button_index = int(event.split('-')[2])
            return button_index
        if event == "-BUTTON-0":
            give_dmg = player.cast_spell(player.spell_book[0])



    window['-OUTPUT-'].update(
        f"GAME OVER",
        text_color='#ffeecc')


if __name__ == "__main__":
        intro()
