'''
Napisz program, który po pobraniu od użytkownika liczby całkowitej dodatniej n wyświetla listę postaci:
1, 2, 3, ..., n 
'''

n = int(input("Podaj liczbę całkowita dodatnią: "))
i = 1

while i < n:
    print(i, end=", ")
    i += 1
print(i)
