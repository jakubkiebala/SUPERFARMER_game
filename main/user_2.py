from interface import view_interface_2
from mechanics import make_choice, type_choice


def game_2():
    while True:
        print(view_interface_2())
        make_choice(type_choice())
        return None
