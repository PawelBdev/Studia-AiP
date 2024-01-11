"""
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią (program ma wymuszać podanie liczby dodatniej),
a następnie wyświetlający na ekranie iloczyn cyfr niezerowych podanej liczby (wszystko z odpowiednimi komunikatami).
"""

while True:
    liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
    if liczba > 0:
        break

x = liczba
iloczyn = 1

while liczba > 0:
    i = liczba % 10
    if i != 0:
        iloczyn *= i
    liczba = liczba // 10
print(f"Iloczyn niezerowych cyfr liczby {x} to: {iloczyn}.")
