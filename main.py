import sys

def send_package():
    print("Podaj dane paczki")
    address = input("Adres: ")
    postal_code = input("Kod pocztowy: ")
    city = input("Miasto: ")
    bank_code = input("Kod z aplikacji banku: ")

    confirmation = input("Wciśnij enter aby potwierdzić")

    if confirmation == '':
        print("Ok, twoja paczka zostanie wkrótce nadana! Dziękujemy i zapraszamy ponownie!")
        return True
    return False

def login():
    print("Wprowadź dane!")
    username = input("Wprowadź login: ")
    password = input("Wprowadź hasło: ")

    if password == 'password' and username == 'Robin91862':
        print("Zalogowano!")
        return True
    else:
        print("Nieprawidłowy login lub hasło.")
        return False

def main():
    print("Witaj w systemie dostawy")
    print("Co chcesz zrobić?")
    print("1 - Wyślij paczkę")
    print("2 - Zaloguj się")

    choice = input()

    if choice == '1':
        if send_package():
            print("Co chcesz zrobić?")
            print("0 - Wyjdź z aplikacji")
            end = input()
            if end == '0':
                sys.exit()
            else:
                sys.exit()

    elif choice == '2':
        if login():
            print("Co chcesz zrobić?")
            print("1 - Wyślij za darmo")
            send_free = input()
            if send_free == '1':
                if send_package():
                    print("Co chcesz zrobić?")
                    print("0 - Wyjdź z aplikacji")
                    end = input()
                    if end == '0':
                        sys.exit()
                    else:
                        sys.exit()
            else:
                sys.exit()
        else:
            sys.exit()

if __name__ == "__main__":
    main()
