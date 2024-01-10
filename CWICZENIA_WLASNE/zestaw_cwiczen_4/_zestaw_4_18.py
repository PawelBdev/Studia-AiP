'''
Napisz program, który po pobraniu od użytkownika liczby całkowitej dodatniej n wyświetla listę list:
1
1, 2
1, 2, 3
...
1, 2, 3, ..., n
'''
n = int(input("liczbę całkowitą dodatnią: "))
while n <= 0:
    n = int(input("Podana liczna nie jest dodatnia. Podaj liczbę całkowitą dodatnią: "))

i = 1
while i < n:
    j = 1
    print(i)
    while j <= i:
        print(j, end=', ')
        j += 1
    i += 1
print(i)
