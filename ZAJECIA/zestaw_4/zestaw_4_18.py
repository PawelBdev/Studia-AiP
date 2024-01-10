'''
Napisz program, który po pobraniu od użytkownika liczby całkowitej dodatniej n wyświetla listę list:
1
1, 2
1, 2, 3
...
1, 2, 3, ..., n
'''

n = int(input("Podaj liczbę całkowita dodatnią: "))
w = 1  # odpowiada za liczbę wierszy
while w <= n:
    i = 1  # odpowiada za liczby w wierszu
    while i < w:
        print(i, end=", ")
        i += 1
    print(i)
    w += 1
