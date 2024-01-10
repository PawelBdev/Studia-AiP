'''

Napisz funkcję dwuargumentową, która 
    dla liczby całkowitej nieujemnej (pierwszy argument) 
        zwraca tę liczbę zamienioną na napis i uzupełnioną w razie potrzeby zerami z przodu. 
        
    Drugi argument funkcji oznacza minimalną liczbę cyfr, za pomocą których ma być zapisana liczba.
Np. dla argumentów 3 i 4 funkcja ma zwrócić "0003", dla argumentów 123 i 4 — "0123", a dla 9876543 i 5 — "9876543".
'''

# a = 3
# b = 4

# if 

def zwroc_zapis(liczba, min_liczba_cyfr):
    liczba = str(liczba)
    return (min_liczba_cyfr - len(liczba)) * "0" + liczba
        
print(zwroc_zapis(3,4))
print(zwroc_zapis(123, 4))
print(zwroc_zapis(9876543, 5))


x = 6