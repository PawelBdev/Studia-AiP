"""
Rozwiązanie zadania umieść w jednym pliku (brakujące nagłówki funkcji zaprojektuj samodzielnie):
a) Napisz funkcję jest_dzielnikiem sprawdzającą, czy pewna dana liczba jest dzielnikiem innej danej liczby.

b) Napisz funkcję o nagłówku
def liczba_dzielnikow(n, pocz, kon):
która zwróci odpowiedź na pytanie, ile jest dzielników liczby n w przedziale ⟨pocz;kon⟩.

c) Napisz funkcję o nagłówku
def liczba_dzielnikow_wspolnych(m, n, pocz, kon):
która znajduje i zwraca liczbę wspólnych dzielników liczb
m  i n  (zakładamy, że obie są dodatnie), ale tylko tych dzielników, które należą do przedziału ⟨pocz;kon⟩
(oba krańce dodatnie). Użyj funkcji jest_dzielnikiem!

d) Zmodyfikuj funkcję jest_dzielnikiem tak, by funkcja z podpunktu c) działała także dla przedziału zawierającego zero.

e*)Zoptymalizuj funkcję z podpunktu c) tak, by nie sprawdzała całego przedziału, lecz jedynie jego sensowną część — użyj którejś z funkcji min3/max3 z wcześniejszego zadania.

f*)Napisz funkcję o nagłówku def liczba_dzielnikow_odrebnych(n, m, pocz, kon): która zwróci odpowiedź na pytanie, ile jest dzielników liczb m oraz n w przedziale ⟨pocz;kon⟩
, które nie dzielą jednocześnie liczb m oraz n.
Uwaga. W zadaniach z podpunktów b), c), f) użyj funkcji jest_dzielnikiem.
"""


def ustal_czy_x_jest_dzielnikiem_y(x: int, y: int) -> bool:
    return True if y % x == 0 else False


def ustal_liczbe_dzielnikow_w_przedziale(n: int, pocz: int, kon: int) -> int:
    liczba_dzielnikow = 0
    while pocz <= kon:
        # if n % pocz == 0:
        if ustal_czy_x_jest_dzielnikiem_y(pocz, n):
            liczba_dzielnikow += 1

        pocz += 1
    return liczba_dzielnikow


def liczba_dzielnikow_wspolnych(m: int, n: int, pocz: int, kon: int) -> int:
    liczba_dzielnikow = 0
    while pocz <= kon:
        print(f"v1 sprawdzam {pocz}")
        if ustal_czy_x_jest_dzielnikiem_y(pocz, m) and ustal_czy_x_jest_dzielnikiem_y(pocz, n):
            liczba_dzielnikow += 1
        pocz += 1
    return liczba_dzielnikow


def liczba_dzielnikow_wspolnych_v2(m: int, n: int, pocz: int, kon: int) -> int:
    liczba_dzielnikow = 0
    if pocz == 0:
        pocz += 1
    while pocz <= kon:
        if ustal_czy_x_jest_dzielnikiem_y(pocz, m) and ustal_czy_x_jest_dzielnikiem_y(pocz, n):
            liczba_dzielnikow += 1
        pocz += 1
    return liczba_dzielnikow


def min2(a, b):
    return a if a <= b else b


def max2(a, b):
    return a if a >= b else b


def min3(a, b, c):
    return min2(min2(a, b), c)


def max3(a, b, c):
    return max2(max2(a, b), c)


def liczba_dzielnikow_wspolnych_v3(m: int, n: int, pocz: int, kon: int) -> int:
    liczba_dzielnikow = 0
    zakres_kon = min3(m, n, kon)
    while pocz <= zakres_kon:
        print(f"v3 sprawdzam {pocz}")
        if ustal_czy_x_jest_dzielnikiem_y(pocz, m) and ustal_czy_x_jest_dzielnikiem_y(pocz, n):
            liczba_dzielnikow += 1
        pocz += 1
    return liczba_dzielnikow


def lista_dzielnikow_w_przedziale(m: int, pocz: int, kon: int) -> int:
    # funkcja pomocnicza do pkt f
    lista_dzielnikow = []
    while pocz <= kon:
        # if n % pocz == 0:
        if ustal_czy_x_jest_dzielnikiem_y(pocz, m):
            lista_dzielnikow.append(pocz)
        pocz += 1
    return lista_dzielnikow


def liczba_dzielnikow_odrebnych(m: int, n: int, pocz: int, kon: int) -> int:
    dzielniki_m = lista_dzielnikow_w_przedziale(m, pocz, kon)
    dzielniki_n = lista_dzielnikow_w_przedziale(n, pocz, kon)
    dzielniki_odrebne = set(dzielniki_n) ^ set(dzielniki_m)
    return len(dzielniki_odrebne)


# print()
# print("ustal_czy_x_jest_dzielnikiem_y(2, 5) -> ", ustal_czy_x_jest_dzielnikiem_y(2, 5))
# print("ustal_czy_x_jest_dzielnikiem_y(7, 14) -> ", ustal_czy_x_jest_dzielnikiem_y(7, 14))
# print()
# print("ustal_liczbe_dzielnikow_w_przedziale(25, 10, 20) -> ", ustal_liczbe_dzielnikow_w_przedziale(25, 10, 20))
# print("ustal_liczbe_dzielnikow_w_przedziale(8, 2, 5) -> ", ustal_liczbe_dzielnikow_w_przedziale(8, 2, 5))
# print()
# print("liczba_dzielnikow_wspolnych(8, 4, 2, 5) -> ", liczba_dzielnikow_wspolnych(8, 4, 2, 5))
# print("liczba_dzielnikow_wspolnych(50, 100, 2, 10) -> ", liczba_dzielnikow_wspolnych(50, 100, 2, 10))
# print()
# print("liczba_dzielnikow_wspolnych_v2(8, 4, 0, 5) -> ", liczba_dzielnikow_wspolnych_v2(8, 4, 0, 5))
# print("liczba_dzielnikow_wspolnych_v2(50, 100, 0, 10) -> ", liczba_dzielnikow_wspolnych_v2(50, 100, 0, 10))
# print()
# print("liczba_dzielnikow_wspolnych_v3(20, 50, 1, 100)", liczba_dzielnikow_wspolnych_v3(20, 50, 1, 100))

# print()
# print("liczba_dzielnikow_wspolnych(20, 50, 1, 100)", liczba_dzielnikow_wspolnych(20, 50, 1, 100))
# print("x" * 30)
# print("liczba_dzielnikow_wspolnych_v3(20, 50, 1, 100)", liczba_dzielnikow_wspolnych_v3(20, 50, 1, 100))

# print()
# print("liczba_dzielnikow_odrebnych", liczba_dzielnikow_odrebnych(8, 12, 1, 8))
