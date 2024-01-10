"""
Napisz funkcję o nagłówku
def wczytaj_liczbe(pocz, kon):
której zadaniem będzie pobranie i zwrócenie od użytkownika liczby całkowitej z przedziału ⟨pocz;kon⟩. Wykorzystaj pętlę zaporową sprawdzającą poprawność pobranych danych. 
"""


def wczytaj_liczbe(pocz, kon):
    liczba = float(input("Podaj liczbę: "))

    while pocz > liczba > kon:
        liczba = float(input("Podano nieprawidlowa liczbę, spróbuj ponownie: "))

    return liczba


start = wczytaj_liczbe(10, 50)

# dokończyć...
