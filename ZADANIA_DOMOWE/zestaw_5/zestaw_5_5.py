"""

""""""
Napisz program wczytujący liczbę naturalną (posłużyć się tu pętlą zaporową blokującą liczby ujemne!) i wypisujący sumę jej cyfr.
Następnie program ma zrobić to samo z wynikiem; i tak w kółko — aż wyświetli w końcu liczbę jednocyfrową.
UWAGA!!! Wyznaczanie sumy cyfr danej liczby naturalnej ma być oddzielną funkcją!!
"""


def zsumuj_cyfry(liczba):
    suma = 0
    while liczba > 0:
        ostatnia = liczba % 10
        suma += ostatnia
        liczba = liczba // 10
    return suma


while True:
    n = int(input("Podaj liczbę naturalną: "))
    if n >= 0:
        break

suma_cyfr = zsumuj_cyfry(n)
print(f"Suma cyfr liczby {n} wynosi {suma_cyfr}.")
