"""
Napisz funkcję o nagłówku
def f(m):
zwracającą m-ty wyraz ciągu Fibonacciego:
"""


def f(m):
    if m == 0:
        wynik = 0
    elif m == 1:
        wynik = 1
    else:
        wynik = f(m - 1) + f(m - 2)
    return wynik


m = int(input("podaj liczbę do ciągu:"))
print(f(m))
