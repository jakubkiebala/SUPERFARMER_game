def type_choice():
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


def make_choice(choice):
    if choice == 1:
        print('Jeden')
    elif choice == 2:
        print('Dwa')
    elif choice == 3:
        print('Trzy')
    elif choice == 4:
        print('cztery')
