"""
Napisz program, który pobiera od użytkownika dwie liczby naturalne i wyznacza
    największy wspólny dzielnik tych liczb oraz
    najmniejszą wspólną wielokrotność.

Zadbaj o poprawność wprowadzanych danych. Wykorzystaj algorytm Euklidesa z dzieleniem.
"""

print("Program wyznacza największy wspólny dzielnik dwóch liczb naturalnych.")

x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))

a = x
b = y

while b:
    a, b = b, a % b

nwd = a
print(f"Największy wspólny dzielnik (NWD) liczb {x} i {y} wynosi {nwd}.")

nww = abs(x * y) / nwd
print(f"Największa wspólna wielokrotność liczb {x} i {y} wynosi {int(nww)}.")
