"""
Zmodyfikuj program z poprzedniego zadania tak, żeby przy pobieraniu liczby n program wymuszał podanie liczby całkowitej dodatniej, tzn. dopóki użytkownik podaje liczbę mniejszą niż jeden program informuje go o błędzie i każe wpisać ponownie.
"""

liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
while liczba <= 0:
    liczba = int(input("Podana liczba nie jest dodatnia. Podaj liczbę całkowitą dodatnią: "))

x = liczba

iloczyn_liczb = 1

while liczba > 0:
    n = float(input("Podaj liczbę: "))
    iloczyn_liczb *= n
    liczba -= 1

print(f"Iloczyn podanych liczby wynosi {iloczyn_liczb}.")
