"""
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią
(program ma wymuszać podanie liczby dodatniej),
a następnie wyświetlający wszystkie jej dzielnki naturalne
(każdy w osobnym wierszu).
"""

n = int(input("liczbę całkowitą dodatnią: "))
while n <= 0:
    n = int(input("Podana liczna nie jest dodatnia. Podaj liczbę całkowitą dodatnią: "))

i = 1
while i <= n // 2:
    if n % i == 0:
        print(i)
    i += 1
print(n)
