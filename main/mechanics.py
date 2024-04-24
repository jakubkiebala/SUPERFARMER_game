from random import choice
from data import UserAnimals
from interface import show_trivia, exchanging_interface

FARM1 = UserAnimals()


# MECHANISM OF INTERFACE #


def type_choice_u1():
    while True:
        do_choice = input('|#| Wprowadź : ')
        try:
            do_choice = int(do_choice)
            if 0 < do_choice < 5:
                return do_choice
            else:
                print('')
                print('|#| Wygląda na to, że podana opcja nie istnieje')
                print('|#| Spróbuj jeszcze raz')
                print('')
        except ValueError:
            print('')
            print('|#| Wprowadzono niepoprawną wartość')
            print('|#| Spróbuj jeszcze raz')
            print('')


def make_choice_u1(do_choice):
    if do_choice == 1:
        roll_the_dices_u1()
    elif do_choice == 2:
        print(FARM1.owned_animals)
        make_choice_u1(type_choice_u1())
    elif do_choice == 3:
        print(exchanging_interface())
        choosing_operations_u1(ask_for_exchange_u1())
    elif do_choice == 4:
        print(show_trivia())
        make_choice_u1(type_choice_u1())


# MECHANISMS OF ROLLING DICES #


def roll_the_dices_u1():
    animal_1 = roll_first_dice_u1()
    animal_2 = roll_second_dice_u1()
    result = (animal_1, animal_2)
    print(f'|#| Na kostkach wypadły : {result}')
    dice_actions_u1(animal_1, animal_2)
    return None


def roll_first_dice_u1():
    # Orange, 1 koń, 1 lis, 2 świnie, 2 owce, 6 królików
    animal_list = ['Koń', 'Lis', 'Świnia', 'Świnia', 'Owca', 'Owca',
                   'Królik', 'Królik', 'Królik', 'Królik', 'Królik', 'Królik'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


def roll_second_dice_u1():
    # Blue, 1 krowa, 1 wilk, 3 owce, 2 świnie, 5 królików
    animal_list = ['Krowa', 'Wilk', 'Owca', 'Owca', 'Owca', 'Świnia', 'Świnia',
                   'Królik', 'Królik', 'Królik', 'Królik', 'Królik'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


def dice_actions_u1(drawn1, drawn2):
    if drawn1 != 'Lis' and drawn2 != 'Wilk':
        first_dice_operating_u1(drawn1, drawn2)
        second_dice_operating_u1(drawn1, drawn2)
    else:
        print('Oh noo')


def first_dice_operating_u1(drawn1, drawn2):
    drawn1_counted = FARM1.owned_animals.count(drawn1)
    if drawn1 == drawn2:
        if drawn1_counted < 2:
            FARM1.add_animal(drawn1)
            print(f'|#| Dodano {drawn1} w liczbie : (1)')
        elif drawn1_counted % 2 == 0:
            half_animals_1 = drawn1_counted // 2
            for i in range(half_animals_1):
                FARM1.add_animal(drawn1)
            print(f'|#| Dodano {drawn1} w liczbie : ({half_animals_1})')
        elif drawn1_counted % 2 != 0:
            half_animals_2 = (drawn1_counted - 1) // 2
            for i in range(half_animals_2):
                FARM1.add_animal(drawn1)
            print(f'|#| Dodano {drawn1} w liczbie : ({half_animals_2})')
    elif drawn1_counted >= 2:
        FARM1.add_animal(drawn1)
        print(f'|#| Dodano {drawn1} w liczbie (1)')
    else:
        print(f'|#| Nie dodano {drawn1}')


def second_dice_operating_u1(drawn1, drawn2):
    drawn2_counted = FARM1.owned_animals.count(drawn2)
    if drawn2 != drawn1:
        if drawn2_counted >= 2:
            FARM1.add_animal(drawn2)
            print(f'|#| Dodano {drawn2} w liczbie (1)')
        else:
            print(f'|#| Nie dodano {drawn2}')
            print('')
            print('>>>>----------------------------------<<<<')


# MECHANISM OF EXCHANGING ANIMALS #


def ask_for_exchange_u1():
    while True:
        question = input('|#| Które zwierze chcesz wymienić : ')
        try:
            question = int(question)
            if 0 < question < 7:
                return question
            else:
                print('')
                print('|#| Wygląda na to, że podana opcja nie istnieje')
                print('|#| Spróbuj jeszcze raz')
                print('')
        except ValueError:
            print('')
            print('|#| Wprowadzono niepoprawną wartość')
            print('|#| Spróbuj jeszcze raz')
            print('')


def choosing_operations_u1(do_ask):
    if do_ask == 1:
        rabbit_operations()
    elif do_ask == 2:
        sheep_operations()
    elif do_ask == 3:
        pig_operations()
    elif do_ask == 4:
        print('Operacje na krowach')
    elif do_ask == 5:
        print('Operacje na koniach')
    elif do_ask == 6:
        print('Powrót do menu')
        make_choice_u1(type_choice_u1())


def rabbit_operations():
    counted_rabbits = FARM1.owned_animals.count('Królik')
    if counted_rabbits < 6:
        print('|#| Nie posiadasz wystarczającej ilości Królików \n'
              '    aby wykonać jakąkolwiek wymianę')
        choosing_operations_u1(ask_for_exchange_u1())
    elif counted_rabbits >= 6:
        print('|#| Możesz wymienić 6 królików na 1 Owcę')
        print('|#| y - tak / n - nie')
        while True:
            question = str(input('|#| Czy chcesz dokonać wymiany? : '))
            if question not in ('y', 'n'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif question == 'y':
                FARM1.exchange_rabbit_sheep()
                print('|#| Otrzymano 1 Owcę')
                rabbit_operations()
                return None
            elif question == 'n':
                choosing_operations_u1(ask_for_exchange_u1())
                return None


def sheep_operations():
    counted_sheep = FARM1.owned_animals.count('Owca')
    if counted_sheep < 1:
        print('|#| Nie posiadasz wystarczającej ilości Owiec \n'
              '    aby wykonać jakąkolwiek wymianę')
        choosing_operations_u1(ask_for_exchange_u1())
    elif 2 > counted_sheep >= 1:
        print('|#| Możesz wymienić 1 Owcę na 6 Królików')
        print('|#| y : tak / n : nie')
        while True:
            question = str(input('|#| Wybierz : '))
            if question not in ('y', 'n'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif question == 'y':
                FARM1.exchange_sheep_rabbit()
                print('|#| Otrzymano 6 Królików')
                sheep_operations()
                return None
            elif question == 'n':
                choosing_operations_u1(ask_for_exchange_u1())
                return None
    elif counted_sheep >= 2:
        print('|#| Możesz wymienić 1 Owcę na 6 Królików \n'
              '    lub wymienić 2 Owce na 1 Świnię')
        print('|#| 1 Owca => 6 Królików : 1 ')
        print('|#| 3 Owce => 1 Świnia : 2 ')
        print('|#| Wyjście : e ')
        while True:
            ask = str(input('|#| Wybierz : '))
            if ask not in ('1', '2', 'e'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif ask == '1':
                FARM1.exchange_sheep_rabbit()
                print('|#| Otrzymano 6 Królików')
                sheep_operations()
                return None
            elif ask == '2':
                FARM1.exchange_sheep_pig()
                print('|#| Otrzymano 1 Świnię')
                sheep_operations()
                return None
            elif ask == 'e':
                choosing_operations_u1(ask_for_exchange_u1())
                return None


def pig_operations():
    pass







for i in range(3):
    FARM1.add_animal('Owca')

rabbit_operations()
print(FARM1.owned_animals)
