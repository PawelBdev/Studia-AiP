"""
Rozwiązanie zadania umieść w jednym pliku (brakujące nagłówki funkcji zaprojektuj samodzielnie):
a) Napisz funkcję jest_dzielnikiem sprawdzającą, czy pewna dana liczba jest dzielnikiem innej danej liczby.

b) Napisz funkcję o nazwie
def suma_dzielnikow(m):
zwracającą sumę dzielników właściwych pewnej danej liczby naturalnej m czyli dzielników należących do przedziału ⟨1;m-1⟩.

c) Napisz funkcję o nazwie
def czy_doskonala(m):
zwracającą odpowiedź na pytanie, czy dana liczba naturalna m jest doskonała. Skorzystaj z funkcji suma_dzielnikow!

d) Napisz funkcję o nazwie
def czy_zaprzyjaznione(m, n):
zwracającą odpowiedź na pytanie, czy dane liczby naturalne m oraz n są ze sobą zaprzyjaźnione. Skorzystaj z funkcji suma_dzielnikow!

"""


def ustal_czy_x_jest_dzielnikiem_y(x, y):
    return True if y % x == 0 else False


def suma_dzielnikow(m):
    suma = 0
    i = 1
    while i <= m / 2:
        if m % i == 0:
            suma += i
        i += 1
    return suma


def czy_doskonala(m):
    return True if suma_dzielnikow(m) == m else False


def czy_zaprzyjaznione(m, n):
    suma_dzielnikow_m = suma_dzielnikow(m)
    suma_dzielnikow_n = suma_dzielnikow(n)
    return True if m == suma_dzielnikow_n and n == suma_dzielnikow_m else False


# print(ustal_czy_x_jest_dzielnikiem_y(5, 15))
# print(ustal_czy_x_jest_dzielnikiem_y(3, 21))
# print(ustal_czy_x_jest_dzielnikiem_y(8, 15))
# print(ustal_czy_x_jest_dzielnikiem_y(8, 80))


# print(suma_dzielnikow(8))
# print(suma_dzielnikow(4))
# print(suma_dzielnikow(3))
# print(suma_dzielnikow(12))
# print(suma_dzielnikow(6))


# print("6", czy_doskonala(6))
# print("12", czy_doskonala(12))
# print("28", czy_doskonala(28))
# print("496", czy_doskonala(496))
# print("500", czy_doskonala(500))


# print(f"220, 284 czy_zaprzyjaznione = {czy_zaprzyjaznione(220, 284)}")
# print(f"1184, 1210 czy_zaprzyjaznione = {czy_zaprzyjaznione(1184, 1210 )}")
# print(f"10, 20 czy_zaprzyjaznione = {czy_zaprzyjaznione(10, 20)}")
# print(f"300, 500 czy_zaprzyjaznione = {czy_zaprzyjaznione(300, 500 )}")
