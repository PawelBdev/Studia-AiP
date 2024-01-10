"""
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią (program ma wymuszać podanie liczby dodatniej),
a następnie wyświetlający na ekranie ile cyfr niezerowych zawiera podana liczba (wszystko z odpowiednimi komunikatami).
"""

while True:
    liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
    if liczba > 0:
        break

x = liczba
licznik = 0

while liczba > 0:
    i = liczba % 10
    if i != 0:
        licznik += 1
    liczba = liczba // 10
print(f"Ilość niezerowych cyfr liczby {x} to: {licznik}.")
