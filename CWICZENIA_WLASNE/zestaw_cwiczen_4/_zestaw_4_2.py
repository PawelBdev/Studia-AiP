'''
Napisz program, który pobiera od użytkownika liczbę całkowitą dodatnią oraz

wyświetla na ekranie wszystkie liczby nieujemne podzielne przez 4

mniejsze od pobranej liczby.
'''

n = int(input("Podaj liczbę całkowitą dodatnią: "))
i = 0

while i < n:
    if i % 4 == 0:
        print(i)
    i += 1

# v2
# while i < n:
#     print(i)
#     i += 4
