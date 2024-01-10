"""
Napisz program wyświetlający średnią
    arytmetyczną,
    geometryczną i
    harmoniczną
n liczb pobranych od użytkownika.

Program ma najpierw pobierać od użytkownika liczbę całkowitą n
(wymusza na użytkowniku podanie liczby dodatniej).

Zakładamy, że użytkownik podaje liczby, z których da się policzyć wszystkie średnie.
"""

# średnia geometryczna jest obliczana jako pierwiastek n-tego stopnia z iloczynu wszystkich liczb

# średnia harmoniczna jest obliczana jako odwrotność średniej arytmetycznej odwrotności tych liczb.
# dla a i b średnia harmoniczna to: 2 / (1/a) + (1/b)
# dla a, b, c średnia harmoniczna to: 3 / (1/a) + (1/b) + (1/c)

while True:
    n = int(input("Podaj liczbę całkowitą dodatnią: "))
    if n > 0:
        break

i = 0
suma = 0
iloczyn = 1
suma_do_sr_harmonijnej = 0

while n > 0:
    i += 1
    n -= 1
    liczba = int(input("Podaj liczbę do obliczen: "))

    suma += liczba
    iloczyn *= liczba
    suma_do_sr_harmonijnej += 1 / liczba


arytmetyczna = suma / i
geometryczna = iloczyn ** (1 / i)
harmoniczna = i / suma_do_sr_harmonijnej

# print("iloczyn: ", iloczyn)
# print("suma_do_sr_harmonijnej: ", suma_do_sr_harmonijnej)
# print('n: ', n)
# print('i: ', i)

print(f"Średnia arytmetyczna podanych liczb to: {arytmetyczna}")
print(f"Średnia geometryczna podanych liczb to: {geometryczna}")
print(f"Średnia harmoniczna podanych liczb to: {harmoniczna}")
