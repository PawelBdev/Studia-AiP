"""
Napisz program, który pobiera długości trzech sąsiednich krawędzi prostopadłościanu
i oblicza (oraz wyświetla) długość jego przekątnej.

"""

a = float(input("Podaj pierwszą krawędź prostopadłościanu: "))
b = float(input("Podaj drugą krawędź prostopadłościanu: "))
c = float(input("Podaj trzecią krawędź prostopadłościanu: "))

# a = 10
# b = 20
# c = 20

d = (a ** 2 + b ** 2 + c ** 2) ** (1 / 2)

print(f"Przekątna prostopadłościanu dla krawędzi o długościach {a}, {b} i {c} wynosi {d}")
