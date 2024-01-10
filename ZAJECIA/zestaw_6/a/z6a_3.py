"""
Napisz funkcję o nagłówku
def losuj(n, a, b):
która losuje i wyświetla na ekranie n liczb całkowitych z przedziału ⟨a;b⟩, ale tak, by każda następna była różna od poprzedniej. Zakładamy, że parametry funkcji są poprawne.

"""
import random as r


def losuj(n, a, b):
    poprzednia = a - 1
    while n > 0:
        liczba = r.randint(a, b)
        while liczba == poprzednia:
            liczba = r.randint(a, b)
        print(liczba)
        poprzednia = liczba
        n -= 1


losuj(4, 1, 2)
