import math

"""
Jedno opakowanie tynku bawełnianego wystarcza na pokrycie 5m2 ściany. 
Stwórz program, który dla podanej przez użytkownika powierzchni ściany 
poda ile opakowań tego tynku potrzeba do jej pokrycia.

Pamiętaj, że odpowiedź musi być podana w postaci liczby naturalnej 
(np. nie można kupić 3.5 opakowania tynku).
"""
wydajnosc_opakowania_mk = 5
powierzchnia = float(input("Podaj powierzchnię ścian: "))

wynik = powierzchnia / wydajnosc_opakowania_mk

liczba_opakowan = math.ceil(wynik)

print(f"Potrzebujesz kupić następującą ilość opakowań: {liczba_opakowan}.")
