'''
Napisz program, który po pobraniu od użytkownika liczby całkowitej dodatniej n wyświetla listę postaci:
1, 2, 3, ..., n 
'''

n = int(input("liczbę całkowitą dodatnią: "))
while n <= 0:
    n = int(input("Podana liczna nie jest dodatnia. Podaj liczbę całkowitą dodatnią: "))

i = 1
while i <= n:
    print(i, end=" ")
    i += 1
