'''
Napisz program, który pobierze od użytkownika dowolny znak nie będący literą (małą ani dużą) ani cyfrą
- należy posłużyć się tu pętlą zaporową blokującą znaki niewłaściwe. 

Następnie program ma wyświetlić zachętę do wpisania liczby z przedziału od 0 do 15 i wczytać liczbę.

Program powinien za każdym razem sprawdzać czy wczytana liczba jest z tego przedziału. 

Jeśli użytkownik 5 razy źle poda liczbę, wówczas ma zostać wyświetlona na ekranie informacja, że program zakończył pracę.

Jeżeli udało się pobrać poprawną liczbę, program ma wyświetlić szlaczek złożony z pobranego znaku wyświetlonego podaną liczbę razy.
'''

while True:
    znak = input("Podaj dowolny znak nie będący literą (małą ani dużą) ani cyfrą: ")
    if not znak.isalnum():
        break
    else:
        print("Podano niewłaściwy znak.")

i = 0
while True:
    liczba = int(input("Podaj liczbę z przedziału od 0 do 15: "))

    if 0 <= liczba <= 15:
        print(znak * liczba)
        break
    else:
        print("Podano niewłaściwą liczbę.")
        i += 1
        if i == 5:
            print("Koniec programu.")
            break
