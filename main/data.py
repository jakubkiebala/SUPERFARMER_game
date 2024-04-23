

class Rounds:
    def __init__(self):
        self.no_rounds = []

    def add_rounds(self):
        self.no_rounds.append(1)
        return self.no_rounds

    def show_rounds(self):
        rounds = sum(self.no_rounds)
        print('')
        print('>>>>----------------------------------<<<<')
        command = f'Trwa runda numer {rounds}'
        return command


class UserAnimals:
    def __init__(self):
        self.owned_animals = ['Królik']

    def add_animal(self, animal):
        self.owned_animals.append(animal)
