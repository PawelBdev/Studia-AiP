"""
Napisz program pobierający od użytkownika współrzędne trzech wierzchołków trójkąta (sześć liczb),
a następnie wyświetlający pole tego trójkąta.
Zakładamy, że podane współrzędne wierzchołków utworzą trójkąt.


"""
print("Podaj współrzętne trzech wierzchołków trójkąta.")
x1 = float(input("Podaj pierwszą współrzędną pierwszego wierzchołka: "))
y1 = float(input("Podaj drugą współrzędną pierwszego wierzchołka: "))
x2 = float(input("Podaj pierwszą współrzędną pierwszego wierzchołka: "))
y2 = float(input("Podaj drugą współrzędną pierwszego wierzchołka: "))
x3 = float(input("Podaj pierwszą współrzędną pierwszego wierzchołka: "))
y3 = float(input("Podaj drugą współrzędną pierwszego wierzchołka: "))

# x1 = 0
# y1 = 0
# x2 = 0
# y2 = 11
# x3 = 20
# y3 = 0

p = 1 / 2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


print(f"Pole trójkąta o wierzchołkach A ({x1}, {y1}), B ({x2}, {y2}), C ({x3}, {y3}) wynosi {p}.")
