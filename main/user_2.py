from interface import view_interface_2
from mechanics_u2 import make_choice_u2, type_choice_u2


def game_2():
    while True:
        print(view_interface_2())
        make_choice_u2(type_choice_u2())
        return None
