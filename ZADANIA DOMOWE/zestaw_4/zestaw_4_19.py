"""
Napisz program pobierający od użytkownika liczbę naturalną, a wyświetlający jej silnię.
"""


while True:
    liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
    if liczba >= 0:
        break

if liczba == 0:
    print("Silnia z 0 wynosi 1.")

else:
    x = liczba
    silnia = 1
    while liczba > 0:
        silnia *= liczba
        liczba -= 1
print(f"Silnia wynosi {silnia}.")
