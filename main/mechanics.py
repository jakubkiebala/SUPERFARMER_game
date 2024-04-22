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
        print('Tutaj będzie rzut kostką i rozpoczęcie tury nowego gracza')
    elif choice == 2:
        print('Tu pojawi się lista zwierząt')
        make_choice(type_choice())
    elif choice == 3:
        print('Tutaj będzie można wymienić zwierzęta, rozpoczęcie tury nowego gracza')
    elif choice == 4:
        print('Tutaj pojawią się wskazówki dotyczące rozgrywki')
        make_choice(type_choice())
