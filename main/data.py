class Rounds:
    def __init__(self):
        self.no_rounds = []

    def add_rounds(self):
        self.no_rounds.append(1)
        return self.no_rounds

    def show_rounds(self):
        rounds = sum(self.no_rounds)
        return f'Trwa runda numer {rounds}'
