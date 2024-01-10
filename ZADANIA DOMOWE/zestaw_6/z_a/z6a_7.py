"""
W pewnej grze każdy z graczy rzuca czterema kośćmi.
Za wynik danego gracza uznawana jest różnica pomiędzy najwyższym a najniższym wynikiem z jego kości
(np. dla wyników 2, 2, 3, 6 wynikiem jest 4).

Napisz funkcję symulującą taki rzut i zwracającą różnicę pomiędzy najniższym a najwyższym wynikiem.
Funkcja ma jeden parametr — liczbę ścian kości (można wykorzystać jedną z funkcji z zadania poprzedniego).

Funkcja ta ma ponadto (w celach testowych) wyświetlać wylosowane wartości.

Ponadto napisz program, który wykona kilka takich losowań (ile i jakimi kośćmi podaje użytkownik) wyświetlając ich wyniki.

Przykład działania programu:

Ile rzutów? 4
Ile ścian? 6
[ wylosowano: 1, 4, 3, 5 ]
Wynik rzutu: 4
[ wylosowano: 5, 5, 3, 2 ]
Wynik rzutu: 3
[ wylosowano: 6, 2, 5, 3 ]
Wynik rzutu: 4
[ wylosowano: 6, 5, 6, 6 ]
Wynik rzutu: 1
"""

from random import randint


def rzut_koscia(s=6):
    return randint(1, s,)


def oblicz_roznice_min_max(lista):
    lista.sort()
    return lista[-1] - lista[0]


def rzut_koscmi(liczba_scian=6):
    wyniki = []
    i = 0
    while i < 4:
        rzut = rzut_koscia(liczba_scian)
        wyniki.append(rzut)
        i += 1
    print(f"[ wylosowano: {', '.join(map(str, wyniki))} ]")
    return oblicz_roznice_min_max(wyniki)


liczba_rzutow = int(input("Ile rzutów? "))
sciany = int(input("Ile ścian? "))

while liczba_rzutow > 0:
    print("Wynik rzutu: ", rzut_koscmi())
    liczba_rzutow -= 1
