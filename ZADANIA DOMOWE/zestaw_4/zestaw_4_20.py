"""
Napisz program obliczający iloczyn liczb pobranych od użytkownika.
Program najpierw pobiera od użytkownika liczbę całkowitą n,
a następnie pobiera n liczb i wyświetla ich iloczyn.
"""


while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba > 0:
        break

x = liczba

iloczyn_liczb = 1
while liczba > 0:
    n = float(input("Podaj liczbę: "))
    iloczyn_liczb *= n
    liczba -= 1

print(f"Iloczyn podanych liczby wynosi {iloczyn_liczb}.")