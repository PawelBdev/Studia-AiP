"""
Napisz program pobierający od użytkownika numer roku i numer miesiąca i wyświetlający liczbę dni w podanym miesiącu. 
"""


def czy_przestepny(rok):
    przestepny = False

    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        przestepny = True

    return przestepny


def liczba_dni(mies, rok):
    przestepny = czy_przestepny(rok)
    if mies in (1, 3, 5, 7, 8, 10, 12):
        wynik = 31
    elif mies == 2:
        wynik = 29 if przestepny else 28
    else:
        wynik = 30
    return wynik


def jest_dzielnikiem(d, n):
    if d != 0 and n % d == 0:
        return True
    else:
        return False


r = int(input("Podaj numer roku: "))
m = int(input("Podaj numer miesiąca: "))

# dni = liczba_dni(m, r)

# print("liczba dni: ", dni)

# Dokończyć!!!!!!!!!!!
