"""
Napisz funkcję o nagłówku
def wczytaj_liczbe(pocz, kon):
której zadaniem będzie pobranie i zwrócenie od użytkownika liczby całkowitej z przedziału ⟨pocz;kon⟩.
Wykorzystaj pętlę zaporową sprawdzającą poprawność pobranych danych.
"""


def wczytaj_liczbe(pocz, kon):
    while True:
        liczba = int(input(f"Podaj liczbę z przedziału <{pocz}, {kon}>: "))
        if pocz <= liczba <= kon:
            return liczba
            # print(f"Poprawnie, liczba {n} należy do przedziału <{pocz}, {kon}>")
            break
        else:
            print(f"Podana liczba nie należy do przedziału <{pocz}, {kon}>.")


poczatek = -5
koniec = 15

print(wczytaj_liczbe(poczatek, koniec))
