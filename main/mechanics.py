def make_choice():
    while True:
        choice = input('Wprowadź : ')
        try:
            choice = int(choice)
            if 0 < choice < 5:
                return choice
            else:
                print('')
                print('Wygląda na to, że podana opcja nie istnieje')
                print('Spróbuj jeszcze raz')
                print('')
        except ValueError:
            print('')
            print('Wprowadzono niepoprawną wartość')
            print('Spróbuj jeszcze raz')
            print('')
