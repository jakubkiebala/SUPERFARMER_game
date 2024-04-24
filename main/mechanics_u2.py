from random import choice
from data import UserAnimals
from interface import show_trivia, exchanging_interface

FARM2 = UserAnimals()

# MECHANISM OF INTERFACE #


def type_choice_u2():
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


def make_choice_u2(do_choice):
    if do_choice == 1:
        roll_the_dices_u2()
    elif do_choice == 2:
        print(FARM2.owned_animals)
        make_choice_u2(type_choice_u2())
    elif do_choice == 3:
        print(exchanging_interface())
        choosing_operations_u2(ask_for_exchange_u2())
    elif do_choice == 4:
        print(show_trivia())
        make_choice_u2(type_choice_u2())

# MECHANISM OF ROLLING DICES #


def roll_the_dices_u2():
    animal_1 = roll_first_dice_u2()
    animal_2 = roll_second_dice_u2()
    result = (animal_1, animal_2)
    print(f'|#| Na kostkach wypadły : {result}')
    dice_actions_u2(animal_1, animal_2)
    return None


def roll_first_dice_u2():
    # Orange, 1 koń, 1 lis, 2 świnie, 2 owce, 6 królików
    animal_list = ['Koń', 'Lis', 'Świnia', 'Świnia', 'Owca', 'Owca',
                   'Królik', 'Królik', 'Królik', 'Królik', 'Królik', 'Królik'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


def roll_second_dice_u2():
    # Blue, 1 krowa, 1 wilk, 3 owce, 2 świnie, 5 królików
    animal_list = ['Krowa', 'Wilk', 'Owca', 'Owca', 'Owca', 'Świnia', 'Świnia',
                   'Królik', 'Królik', 'Królik', 'Królik', 'Królik'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


def dice_actions_u2(drawn1, drawn2):
    if drawn1 != 'Lis' and drawn2 != 'Wilk':
        first_dice_operating_u2(drawn1, drawn2)
        second_dice_operating_u2(drawn1, drawn2)
    else:
        print('Oh noo')


def first_dice_operating_u2(drawn1, drawn2):
    drawn1_counted = FARM2.owned_animals.count(drawn1)
    if drawn1 == drawn2:
        if drawn1_counted < 2:
            FARM2.add_animal(drawn1)
            print(f'|#| Dodano {drawn1} w liczbie : (1)')
        elif drawn1_counted % 2 == 0:
            half_animals_1 = drawn1_counted // 2
            for i in range(half_animals_1):
                FARM2.add_animal(drawn1)
            print(f'|#| Dodano {drawn1} w liczbie : ({half_animals_1})')
        elif drawn1_counted % 2 != 0:
            half_animals_2 = (drawn1_counted - 1) // 2
            for i in range(half_animals_2):
                FARM2.add_animal(drawn1)
            print(f'|#| Dodano {drawn1} w liczbie : ({half_animals_2})')
    elif drawn1_counted >= 2:
        FARM2.add_animal(drawn1)
        print(f'|#| Dodano {drawn1} w liczbie (1)')
    else:
        print(f'|#| Nie dodano {drawn1}')


def second_dice_operating_u2(drawn1, drawn2):
    drawn2_counted = FARM2.owned_animals.count(drawn2)
    if drawn2 != drawn1:
        if drawn2_counted >= 2:
            FARM2.add_animal(drawn2)
            print(f'|#| Dodano {drawn2} w liczbie (1)')
        else:
            print(f'|#| Nie dodano {drawn2}')

# MECHANISM OF EXCHANGING ANIMALS #


def ask_for_exchange_u2():
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


def choosing_operations_u2(do_ask):
    if do_ask == 1:
        rabbit_operations()
    elif do_ask == 2:
        sheep_operations()
    elif do_ask == 3:
        pig_operations()
    elif do_ask == 4:
        cow_operations()
    elif do_ask == 5:
        print('Ihaahaaa')
        choosing_operations_u2(ask_for_exchange_u2())
    elif do_ask == 6:
        print('Powrót do menu')
        make_choice_u2(type_choice_u2())


def rabbit_operations():
    counted_rabbits = FARM2.owned_animals.count('Królik')
    if counted_rabbits < 6:
        print('|#| Nie posiadasz wystarczającej ilości Królików \n'
              '    aby wykonać jakąkolwiek wymianę')
        choosing_operations_u2(ask_for_exchange_u2())
    elif counted_rabbits >= 6:
        print('|#| Możesz wymienić 6 królików na 1 Owcę')
        print('|#| y - tak / n - nie')
        while True:
            question = str(input('|#| Czy chcesz dokonać wymiany? : '))
            if question not in ('y', 'n'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif question == 'y':
                FARM2.exchange_rabbit_sheep()
                print('|#| Otrzymano 1 Owcę')
                rabbit_operations()
                return None
            elif question == 'n':
                choosing_operations_u2(ask_for_exchange_u2())
                return None


def sheep_operations():
    counted_sheep = FARM2.owned_animals.count('Owca')
    if counted_sheep < 1:
        print('|#| Nie posiadasz wystarczającej ilości Owiec \n'
              '    aby wykonać jakąkolwiek wymianę')
        choosing_operations_u2(ask_for_exchange_u2())
    elif 2 > counted_sheep >= 1:
        print('|#| Możesz wymienić 1 Owcę na 6 Królików')
        print('|#| y : tak / n : nie')
        while True:
            question = str(input('|#| Wybierz : '))
            if question not in ('y', 'n'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif question == 'y':
                FARM2.exchange_sheep_rabbit()
                print('|#| Otrzymano 6 Królików')
                sheep_operations()
                return None
            elif question == 'n':
                choosing_operations_u2(ask_for_exchange_u2())
                return None
    elif counted_sheep >= 2:
        print('|#| Możesz wymienić 1 Owcę na 6 Królików \n'
              '    lub wymienić 2 Owce na 1 Świnię')
        print('|#| 1 Owca => 6 Królików : 1 ')
        print('|#| 2 Owce => 1 Świnia : 2 ')
        print('|#| Wyjście : e ')
        while True:
            ask = str(input('|#| Wybierz : '))
            if ask not in ('1', '2', 'e'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif ask == '1':
                FARM2.exchange_sheep_rabbit()
                print('|#| Otrzymano 6 Królików')
                sheep_operations()
                return None
            elif ask == '2':
                FARM2.exchange_sheep_pig()
                print('|#| Otrzymano 1 Świnię')
                sheep_operations()
                return None
            elif ask == 'e':
                choosing_operations_u2(ask_for_exchange_u2())
                return None


def pig_operations():
    counted_pigs = FARM2.owned_animals.count('Świnia')
    if counted_pigs < 1:
        print('|#| Nie posiadasz wystarczającej ilości Świń \n'
              '    aby wykonać jakąkolwiek wymianę')
        choosing_operations_u2(ask_for_exchange_u2())
    elif 3 > counted_pigs >= 1:
        print('|#| Możesz wymienić 1 Świnię na 2 Owce')
        print('|#| y : tak / n : nie')
        while True:
            question = str(input('|#| Wybierz : '))
            if question not in ('y', 'n'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif question == 'y':
                FARM2.exchange_pig_sheep()
                print('|#| Otrzymano 2 Owce')
                pig_operations()
                return None
            elif question == 'n':
                choosing_operations_u2(ask_for_exchange_u2())
                return None
    elif counted_pigs >= 3:
        print('|#| Możesz wymienić 1 Świnię na 2 Owce \n'
              '    lub wymienić 3 Świnie na 1 Krowę')
        print('|#| 1 Świnia => 2 Owce : 1 ')
        print('|#| 3 Świnie => 1 Krowa : 2 ')
        print('|#| Wyjście : e ')
        while True:
            ask = str(input('|#| Wybierz : '))
            if ask not in ('1', '2', 'e'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif ask == '1':
                FARM2.exchange_pig_sheep()
                print('|#| Otrzymano 2 Owce')
                pig_operations()
                return None
            elif ask == '2':
                FARM2.exchange_pig_cow()
                print('|#| Otrzymano 1 Krowę')
                pig_operations()
                return None
            elif ask == 'e':
                choosing_operations_u2(ask_for_exchange_u2())
                return None


def cow_operations():
    counted_cows = FARM2.owned_animals.count('Krowa')
    if counted_cows < 1:
        print('|#| Nie posiadasz wystarczającej ilości Krów \n'
              '    aby wykonać jakąkolwiek wymianę')
        choosing_operations_u2(ask_for_exchange_u2())
    elif 2 > counted_cows >= 1:
        print('|#| Możesz wymienić 1 Krowę na 3 Świnie')
        print('|#| y : tak / n : nie')
        while True:
            question = str(input('|#| Wybierz : '))
            if question not in ('y', 'n'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif question == 'y':
                FARM2.exchange_cow_pig()
                print('|#| Otrzymano 3 Świnie')
                cow_operations()
                return None
            elif question == 'n':
                choosing_operations_u2(ask_for_exchange_u2())
                return None
    elif counted_cows >= 2:
        print('|#| Możesz wymienić 1 Krowę na 3 Świnie \n'
              '    lub wymienić 2 Krowy na 1 Konia')
        print('|#| 1 Krowa => 3 Świnie : 1 ')
        print('|#| 2 Krowy => 1 Koń : 2 ')
        print('|#| Wyjście : e ')
        while True:
            ask = str(input('|#| Wybierz : '))
            if ask not in ('1', '2', 'e'):
                print('|#| Podano złą wartość, spróbuj jeszcze raz')
            elif ask == '1':
                FARM2.exchange_cow_pig()
                print('|#| Otrzymano 3 Świnie')
                cow_operations()
                return None
            elif ask == '2':
                FARM2.exchange_cow_horse()
                print('|#| Otrzymano 1 Konia')
                cow_operations()
                return None
            elif ask == 'e':
                choosing_operations_u2(ask_for_exchange_u2())
                return None
