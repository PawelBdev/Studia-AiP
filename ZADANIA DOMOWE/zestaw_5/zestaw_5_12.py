"""
Rozwiązanie zadania umieść w jednym pliku (brakujące nagłówki funkcji zaprojektuj samodzielnie):
a) Napisz funkcję sprawdzającą, czy pewna dana liczba jest dzielnikiem innej danej liczby.

b) Napisz funkcję zwracającą liczbę wszystkich dzielników danej liczby.

c) Napisz funkcję sprawdzająca, czy dana liczba jest liczbą pierwszą.

d*)Napisz funkcję o nagłówku
def liczba_dzielnikow_pierwszych_bp(m):
zwracającą liczbę dzielników pierwszych liczby m liczonych bez powtórzeń (to jest dla m=8 wynikiem będzie 1).

e*)Napisz funkcję o nagłówku
def liczba_dzielnikow_pierwszych_zp(m):
zwracającą liczbę dzielników pierwszych liczby m liczonych z powtórzeniami (to jest dla m=8 wynikiem będzie 3).

f*)Napisz funkcję o nagłówku
def czy_polpierwsza(m):
zwracającą odpowiedź na pytanie, czy liczba m jest półpierwsza. Skorzystaj z funkcji liczba_dzielnikow_pierwszych_zp!
"""


def czy_x_jest_dzielnikiem_y(x, y):
    return True if y % x == 0 else False


def zwroc_dzielniki_liczby(x: int) -> list:
    dzielniki = []
    i = 1
    while i <= x / 2:
        if x % i == 0:
            dzielniki.append(i)
        i += 1
    dzielniki.append(x)
    return dzielniki


def czy_liczba_pierwsza(x: int) -> bool:
    dzielniki = []
    i = 1
    while i <= x / 2:
        if x % i == 0:
            dzielniki.append(i)
        i += 1
    return True if len(dzielniki) == 1 else False


def liczba_dzielnikow_pierwszych_bp(m: int) -> int:
    dzielniki = zwroc_dzielniki_liczby(m)
    dzielniki_pierwsze = [d for d in dzielniki if czy_liczba_pierwsza(d)]
    return len(dzielniki_pierwsze)


def liczba_dzielnikow_pierwszych_zp(m: int) -> int:
    dzielniki = zwroc_dzielniki_liczby(m)
    dzielniki_pierwsze = [d for d in dzielniki if czy_liczba_pierwsza(d)]

    dzielniki_pierwsze_z_powtorkami = []
    ilosc_dziel_pierwszych = len(dzielniki_pierwsze)

    while m > 1:
        i = 0
        while i < ilosc_dziel_pierwszych:
            if czy_x_jest_dzielnikiem_y(dzielniki_pierwsze[i], m):
                dzielniki_pierwsze_z_powtorkami.append(dzielniki_pierwsze[i])
                break
            else:
                i += 1
        m = m / dzielniki_pierwsze[i]
    liczba_dzielnikow_pierwsze_z_powtorkami = len(dzielniki_pierwsze_z_powtorkami)
    return liczba_dzielnikow_pierwsze_z_powtorkami


def czy_polpierwsza(m: int) -> bool:
    return True if liczba_dzielnikow_pierwszych_zp(m) == 2 else False


print()
print(f"czy_x_jest_dzielnikiem_y(7, 70) -> {czy_x_jest_dzielnikiem_y(7, 70)}")
print(f"czy_x_jest_dzielnikiem_y(7, 13) -> {czy_x_jest_dzielnikiem_y(7, 13)}")
print(f"czy_x_jest_dzielnikiem_y(7, 140) -> {czy_x_jest_dzielnikiem_y(7, 140)}")
print()
print(f"zwroc_dzielniki_liczby(8) -> {zwroc_dzielniki_liczby(8)}")
print(f"zwroc_dzielniki_liczby(17) -> {zwroc_dzielniki_liczby(17)}")
print(f"zwroc_dzielniki_liczby(108) -> {zwroc_dzielniki_liczby(1018)}")
print()
print(f"czy_liczba_pierwsza(13) -> {czy_liczba_pierwsza(13)}")
print(f"czy_liczba_pierwsza(27) -> {czy_liczba_pierwsza(27)}")
print()
print(f"liczba_dzielnikow_pierwszych_bp(8) -> {liczba_dzielnikow_pierwszych_bp(8)}")
print(f"liczba_dzielnikow_pierwszych_bp(17) -> {liczba_dzielnikow_pierwszych_bp(17)}")
print(f"liczba_dzielnikow_pierwszych_bp(108) -> {liczba_dzielnikow_pierwszych_bp(108)}")
print(f"liczba_dzielnikow_pierwszych_bp(228) -> {liczba_dzielnikow_pierwszych_bp(228)}")
print()
print(f"liczba_dzielnikow_pierwszych_zp(8) -> {liczba_dzielnikow_pierwszych_zp(8)}")
print(f"liczba_dzielnikow_pierwszych_zp(17) -> {liczba_dzielnikow_pierwszych_zp(17)}")
print(f"liczba_dzielnikow_pierwszych_zp(108) -> {liczba_dzielnikow_pierwszych_zp(108)}")
print(f"liczba_dzielnikow_pierwszych_zp(228) -> {liczba_dzielnikow_pierwszych_zp(228)}")
print()
print(f"czy_polpierwsza(33) -> {czy_polpierwsza(33)}")
print(f"czy_polpierwsza(35) -> {czy_polpierwsza(35)}")
print(f"czy_polpierwsza(40) -> {czy_polpierwsza(40)}")
print()
