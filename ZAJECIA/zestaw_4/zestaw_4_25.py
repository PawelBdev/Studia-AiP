''''
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią (program ma wymuszać podanie liczby dodatniej), 
a następnie wyświetlający wszystkie jej dzielniki naturalne 
(każdy w osobnym wierszu).

'''

while True:
    n = int(input("Podaj dodatnią: "))
    if n > 0:
        break

d = 1
while d <= n // 2:
    if n % d == 0:
        print(d)
    d += 1
print(n)
