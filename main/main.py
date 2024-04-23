from data import Rounds
from interface import welcome_sign
from user_1 import game_1
from user_2 import game_2

rounds = Rounds()


def game_user1():
    rounds.add_rounds()
    print(rounds.show_rounds())
    game_1()
    game_user2()


def game_user2():
    game_2()
    game_user1()


print(welcome_sign())
game_user1()
