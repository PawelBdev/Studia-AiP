def min2(a, b):
    return a if a < b else b


def max2(a, b):
    return a if a > b else b


def min3(a, b, c):
    x = min2(a, b)
    return min2(x, c)


def max3(a, b, c):
    x = max2(a, b)
    return max(x, c)


def srodkowa_z_3(a, b, c):
    x = min3(a, b, c)
    y = max3(a, b, c)
    return (x + y) / 2


a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
c = float(input("Podaj liczbę c: "))

test_min = min(a, b)
print(f"test_min = {test_min}")

test_max = max2(a, b)
print(f"test_max = {test_max}")

test_min3 = min3(a, b, c)
print(f"test_min3 = {test_min3}")

test_max3 = max3(a, b, c)
print(f"test_max3 = {test_max3}")

test_srodkowa_z_3 = srodkowa_z_3(a, b, c)
print(f"test_srodkowa_z_3 = {test_srodkowa_z_3}")
