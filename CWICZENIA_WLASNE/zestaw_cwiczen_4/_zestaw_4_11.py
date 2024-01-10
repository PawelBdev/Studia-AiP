'''
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią
    (program ma wymuszać podanie liczby nieujemnej),

a następnie wyświetlający na ekranie informację,
ile cyfr ma podana liczba (wszystko z odpowiednimi komunikatami).
'''

n = int(input("liczbę całkowitą dodatnią: "))
while n <= 0:
    n = int(input("Podana liczna nie jest dodatnia. Podaj liczbę całkowitą dodatnią: "))

i = n
ilosc_cyfr = 0

while i > 0:
    i = i // 10
    ilosc_cyfr += 1

print(f"Ilość cyfr w liczbie {n} wynosi {ilosc_cyfr}.")
