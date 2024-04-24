

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

    def exchange_rabbit_sheep(self):
        for i in range(6):
            self.owned_animals.remove('Królik')
        self.add_animal('Owca')

    def exchange_sheep_rabbit(self):
        self.owned_animals.remove('Owca')
        for i in range(6):
            self.add_animal('Królik')

    def exchange_sheep_pig(self):
        for i in range(2):
            self.owned_animals.remove('Owca')
        self.add_animal('Świnia')
