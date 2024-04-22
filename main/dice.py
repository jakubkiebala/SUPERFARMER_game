from random import choice


def roll_first_dice():
    # Orange, 1 koń, 1 lis, 2 świnie, 2 owce, 6 królików
    animal_list = ['Horse', 'Fox', 'Pig', 'Pig', 'Sheep', 'Sheep',
                   'Rabbit', 'Rabbit', 'Rabbit', 'Rabbit', 'Rabbit', 'Rabbit'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


def roll_second_dice():
    # Blue, 1 krowa, 1 wilk, 3 owce, 2 świnie, 5 królików
    animal_list = ['Cow', 'Wolf', 'Sheep', 'Sheep', 'Sheep', 'Pig', 'Pig',
                   'Rabbit', 'Rabbit', 'Rabbit', 'Rabbit', 'Rabbit'
                   ]
    drawn_animal = choice(animal_list)
    return drawn_animal


print(roll_first_dice())
print(roll_second_dice())
