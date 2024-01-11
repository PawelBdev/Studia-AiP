"""
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią (program ma wymuszać podanie liczby dodatniej),
a następnie wyświetlający na ekranie sumę cyfr podanej liczby (wszystko z odpowiednimi komunikatami).
"""

while True:
    liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
    if liczba > 0:
        break

x = liczba
suma = 0
while liczba > 0:
    i = liczba % 10
    suma += i
    liczba = liczba // 10
print(f"Suma cyfr liczby {x} wynosi: {suma}.")
