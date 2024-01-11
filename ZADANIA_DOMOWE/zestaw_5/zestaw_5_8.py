"""
Napisz funkcję logiczną chce_dalej, która zwraca wartość True, gdy użytkownik odpowie 't' lub 'T' na pytanie 'Czy chcesz kontynować?', False w przeciwnym razie.
"""


def chce_dalej():
    czy_kont = input("Czy chcesz kontynować? ")
    return True if czy_kont.lower() == 't' else False


print(chce_dalej())
