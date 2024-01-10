import math


def f(x):
    return abs(x) ** (1 / 2) + math.sin(x) / (1 + x**2)


def g(x):
    if x > 0:
        return f(x)
    elif -1 <= x <= 0:
        return -(abs(f(x) ** (1 / 3)))
    else:
        return 0


x = float(input("Podaj liczbę: "))


wynik_f = round(f(x), 4)
wynik_g = round(g(x), 4)

print(
    "Wynik dla liczby {}: \n \t f(x): {:7.4f} \n \t g(x): {:7.4f}".format(
        x, wynik_f, wynik_g
    )
)
