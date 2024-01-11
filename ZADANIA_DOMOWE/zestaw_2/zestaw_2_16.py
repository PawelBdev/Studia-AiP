# Pobranie 9 liczb od użytkownika
a = float(input("Wprowadź współczynnik [1][1]: "))
b = float(input("Wprowadź współczynnik [1][2]: "))
c = float(input("Wprowadź współczynnik [1][3]: "))
d = float(input("Wprowadź współczynnik [2][1]: "))
e = float(input("Wprowadź współczynnik [2][2]: "))
f = float(input("Wprowadź współczynnik [2][3]: "))
g = float(input("Wprowadź współczynnik [3][1]: "))
h = float(input("Wprowadź współczynnik [3][2]: "))
i = float(input("Wprowadź współczynnik [3][3]: "))

# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# g = 7
# h = 8
# i = 9

# Utworzenie macierzy
macierz = [[a, b, c], [d, e, f], [g, h, i]]

# Wyświetlenie macierzy
print("Macierz 3x3:")
for wiersz in macierz:
    print(wiersz)

wyznacznik = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
print(f"Wyznacznik macierzy: {wyznacznik}")

slad = a + e + i
print(f"Ślad macierzy: {slad}")
