from interface import view_interface_1
from mechanics import type_choice_u1, make_choice_u1


def game_1():
    while True:
        print(view_interface_1())
        make_choice_u1(type_choice_u1())
        return None
