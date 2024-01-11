"""
Zmodyfikuj program z poprzedniego zadania tak, żeby w przypadku wpisania przez użytkownika zera jako jednego z czynników program od razu kończył działanie bez pobierania kolejnych liczb. Program ma w tej sytuacji wyświetlić komunikat o tym, że niezależnie od kolejnych czynników wynik będzie wynosił zero.
Wskazówka: wykorzystaj instrukcję przerywania działania pętli
"""

liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
while liczba <= 0:
    liczba = int(input("Podana liczba nie jest dodatnia. Podaj liczbę całkowitą dodatnią: "))

x = liczba

iloczyn_liczb = 1

while liczba > 0:
    n = float(input("Podaj liczbę: "))
    if n == 0:
        print("Koniec programu. Wynik wynosi 0.")
        break
    iloczyn_liczb *= n
    liczba -= 1

if n != 0:
    print(f"Iloczyn podanych liczby wynosi {iloczyn_liczb}.")
