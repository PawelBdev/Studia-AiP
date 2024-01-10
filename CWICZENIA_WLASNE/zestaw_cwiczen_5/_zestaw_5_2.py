'''
W tym zadaniu nie korzystaj ze standardowych funkcji min oraz max. Rozwiązanie zadania umieść w jednym pliku:
Napisz funkcje o nagłówkach
def min2(a, b):
def max2(a, b):
które zwracają odpowiednio mniejszą lub większą z podanych liczb.

Napisz funkcje o nagłówkach
def min3(a, b, c):
def max3(a, b, c):
które zwracają odpowiednio mniejszą lub większą z podanych liczb. Nie używaj instrukcji if, za to użyj koniecznie funkcji z poprzedniego podpunktu!

(*)Napisz funkcję o nagłówku
def srodkowa_z_3(a, b, c):
które zwracają środkową (co do wartości, czyli medianę) z podanych liczb. Najlepiej nie używaj instrukcji if, za to użyj funkcji z poprzednich podpunktów!

Napisz program testujący napisane funkcje.
'''


def min2(a, b):
    return a if a <= b else b


def max2(a, b):
    return a if a >= b else b


def min3(a, b, c):
    return min2(min2(a, b), c)


def max3(a, b, c):
    return max2(max2(a, b), c)


print(min3(5, 7, 12))
print(max3(5, 7, 12))

