from interface import view_interface_1
from mechanics import make_choice


def game_1():
    while True:
        print(view_interface_1())
        make_choice()

        return None