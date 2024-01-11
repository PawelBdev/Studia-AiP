"""
Napisz program, który wczytuje ze standardowego wejścia trzy liczby,
a następnie wyznacza ich średnią arytmetyczną, geometryczną i harmoniczną.
"""

print("Podaj trzy dowolne liczby.")

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))

# a = 1
# b = 10
# c = 15

srednia_arytmetyczna = (a + b + c) / 3
srednia_geometryczna = (a * b * c) ** (1 / 3)
srednia_harmoniczna = 3 / (1 / a + 1 / b + 1 / c)

print(f"Dla liczb {a}, {b}, {c} średnie wynoszą:")
print(f"Średna arytmetyczna: {srednia_arytmetyczna}")
print(f"Średna geometryczna: {srednia_geometryczna}")
print(f"Średna harmoniczna: {srednia_harmoniczna}")
