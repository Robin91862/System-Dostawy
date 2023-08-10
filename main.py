import sys

print("Witaj w systemie DPD")

print("Co chcesz zrobić?")

print("1 - Wyślij paczkę")

print("2 - Zaloguj się")

wybór = input()


if wybór == '1':
    print("Podaj dane paczki")

    input("Adres: ")

    input("Kod pocztowy: ")

    input("Miasto: ")

    input("Kod BLIK: ")
    
    skończenieWpisywaniaAdresu = input("Wciśnij Enter")

    if skończenieWpisywaniaAdresu == '':
        print("Ok, twoja paczka zostanie wkrótce nadana! Dziękujemy i zapraszamy ponownie!")
        print()
        print("Co chcesz zrobić?")
        print("0 - Wyjdź z aplikacji")
        zakończenie = input()
        if zakończenie == '0':
            sys.exit()

if wybór == '2':
    print("Wprowadź dane!")
    login = input("Wprowadź login: ")
    hasło = input("Wprowadź hasło: ")
    if hasło == 'password' and login == 'Robin91862':
        print("Zalogowano!")
        print("Co chcesz zrobić?")
        print("1 - Wyślij za darmo")
        wyślij = input()
        if wyślij == '1':
            print("Podaj dane paczki")

            input("Adres: ")

            input("Kod pocztowy: ")

            input("Miasto: ")

            skończenieWpisywaniaAdresu2 = input("Wciśnij Enter")

        if skończenieWpisywaniaAdresu2 == '':
                print("Ok, twoja paczka zostanie wkrótce nadana! Dziękujemy i zapraszamy ponownie!")
                print()
                print("Co chcesz zrobić?")
                print("0 - Wyjdź z aplikacji")
                zakończenie2 = input()
                if zakończenie2 == '0':
                    sys.exit()
    else:print("Wprowadzono błędne dane!")
    print()
    print("Co chcesz zrobić?")
    print("0 - Wyjdź z aplikacji")
    zakończenie3 = input()
    if zakończenie3 == '0':
        sys.exit()
