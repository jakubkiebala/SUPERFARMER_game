from random import choice
from main.data import UserAnimals

FARM = UserAnimals()


def roll_the_dices():
    animal_1 = roll_first_dice()
    animal_2 = roll_second_dice()
    result = (animal_1, animal_2)
    print(f'|#| Na kostkach wypadły : {result}')
    dice_actions(animal_1, animal_2)
    return None


def roll_first_dice():
    # Orange, 1 koń, 1 lis, 2 świnie, 2 owce, 6 królików
    animal_list = ['Koń', 'Lis', 'Świnia', 'Świnia', 'Owca', 'Owca',
                   'Królik', 'Królik', 'Królik', 'Królik', 'Królik', 'Królik'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


def roll_second_dice():
    # Blue, 1 krowa, 1 wilk, 3 owce, 2 świnie, 5 królików
    animal_list = ['Krowa', 'Wilk', 'Owca', 'Owca', 'Owca', 'Świnia', 'Świnia',
                   'Królik', 'Królik', 'Królik', 'Królik', 'Królik'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


def dice_actions(drawn1, drawn2):
    if drawn1 != 'Lis':
        dice_operating(drawn1, drawn2)
        pass
    else:
        print('Oh noo')


def dice_operating(drawn1, drawn2):
    drawn1_counted = FARM.owned_animals.count(drawn1)
    print(drawn1_counted)
    if drawn1 == drawn2:
        if drawn1_counted < 2:
            FARM.add_animal(drawn1)
            print(f'|1| Dodano {drawn1} w liczbie : (1)')
        elif drawn1_counted % 2 == 0:
            half_animals_1 = drawn1_counted // 2
            for i in range(half_animals_1):
                FARM.add_animal(drawn1)
            print(f'|2| Dodano {drawn1} w liczbie : ({half_animals_1})')
        elif drawn1_counted % 2 != 0:
            half_animals_2 = (drawn1_counted - 1) // 2
            for i in range(half_animals_2):
                FARM.add_animal(drawn1)
            print(f'|3| Dodano {drawn1} w liczbie : ({half_animals_2})')
    elif drawn1_counted >= 2:
        FARM.add_animal(drawn1)
        print(f'|4| Dodano {drawn1} w liczbie (1)')
    else:
        print(f'|5| Nie dodano {drawn1}')


roll_the_dices()

