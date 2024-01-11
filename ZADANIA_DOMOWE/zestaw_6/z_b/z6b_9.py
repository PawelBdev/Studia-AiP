'''

Napisz funkcję dwuargumentową, która 
    dla liczby całkowitej nieujemnej (pierwszy argument) 
        zwraca tę liczbę zamienioną na napis i uzupełnioną w razie potrzeby zerami z przodu. 

    Drugi argument funkcji oznacza minimalną liczbę cyfr, za pomocą których ma być zapisana liczba.
Np. dla argumentów 3 i 4 funkcja ma zwrócić "0003", dla argumentów 123 i 4 — "0123", a dla 9876543 i 5 — "9876543".
'''


def zamien_liczbe_na_napis(liczba, min_liczba_cyfr):
    napis = str(liczba)
    if min_liczba_cyfr > len(napis):
        roznica = min_liczba_cyfr - len(napis)
        return '0' * roznica + napis
    else:
        return napis


liczba = int(input("Podaj liczbę całkowitą nieujemną: "))
min_liczba_cyfr = int(input("Podaj minimalną liczbę cyfr: "))

print(zamien_liczbe_na_napis(liczba, min_liczba_cyfr))
