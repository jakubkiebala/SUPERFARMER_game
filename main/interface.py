def view_interface_1():
    interface = """
    +---------------+
    |Tura gracza (1)|
    +---------------+----------------+
    |(1) - rzuć kostką               |
    |(2) - pokaż posiadane zwierzęta |
    |(3) - wymień zwierzęta          |
    |(4) - tablica podpowiedzi       |
    +--------------------------------+
    """
    return interface


def view_interface_2():
    interface = """
    +---------------+
    |Tura gracza (2)|
    +---------------+----------------+
    |(1) - rzuć kostką               |
    |(2) - pokaż posiadane zwierzęta |
    |(3) - wymień zwierzęta          |
    |(4) - tablica podpowiedzi       |
    +--------------------------------+
    """
    return interface

def welcome_sign():
    sign = """
#==========================================#
|                                          |
|    ______+      ________       ____      |
|   /   ___|      |  ____|      /    \     |
|   \   \         |  |____     /  /\  \    |
|    \   \        |   ___|    /  /__\  \   |
|  __/   / ___    |  |       /  /----\  \  |
| |_____/  \_/    |__|      /__/      \__\ |
|                                          |
#==========================================#   
    """
    return sign


def show_trivia():
    trivia = """
     +--------------------------------+
     |       (Wymiana Zwierząt)       |
     |      6 Królików == 1 Owca      |
     |       2 Owce == 1 Świnia       |
     |       3 Świnie == 1 Krowa      |
     |       2 Krowy == 1 Koń         |
     +--------------------------------+
    """
    return trivia


def exchanging_interface():
    interface = """
  +-------------------------+
  |(1) - Królik| (2) - Owca |
  |(3) - Świnia| (4) - Krowa|
  |(5) - Koń   | (6) - WYJDŹ|
  +-------------------------+
    """
    return interface
