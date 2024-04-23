from random import choice
from data import UserAnimals
FARM1 = UserAnimals()


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
        print('Tutaj będzie można wymienić zwierzęta, rozpoczęcie tury nowego gracza')
    elif do_choice == 4:
        print('Tutaj pojawią się wskazówki dotyczące rozgrywki')
        make_choice_u1(type_choice_u1())


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
            FARM1.add_animal(drawn1)
            print(f'|#| Dodano {drawn2} w liczbie (1)')
        else:
            print(f'|#| Nie dodano {drawn2}')
            print('')
            print('>>>>----------------------------------<<<<')
