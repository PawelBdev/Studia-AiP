"""
(*)Popraw program z poprzedniego zadania tak, żeby w przypadku podania przez użytkownika liczb,
z których nie da się policzyć którejś ze średnich 
(możesz założyć, że
    średnią geometryczną można liczyć tylko z liczb nieujemnych, a 
    harmoniczną — z niezerowych) 

program wyświetlał o tym informację (ale liczył pozostałe średnie).

-----------------------------------------------------------------
Treść poprzedniego:

Napisz program wyświetlający średnią
    arytmetyczną,
    geometryczną i
    harmoniczną
n liczb pobranych od użytkownika.

Program ma najpierw pobierać od użytkownika liczbę całkowitą n

"""


n = int(input("Podaj liczbę całkowitą: "))

i = 0
suma = 0
iloczyn = 1
suma_do_sr_harmonijnej = 0

podano_zero = False
podano_ujemna = False

while n > 0:
    i += 1
    n -= 1
    liczba = int(input("Podaj liczbę do obliczen: "))

    if liczba == 0:
        podano_zero = True

    if liczba < 0:
        podano_ujemna = True

    if not podano_zero:
        suma_do_sr_harmonijnej += 1 / liczba

    suma += liczba
    iloczyn *= liczba


arytmetyczna = suma / i
print(f"Średnia arytmetyczna podanych liczb to: {arytmetyczna}")

if not podano_ujemna:
    geometryczna = iloczyn ** (1 / i)
    print(f"Średnia geometryczna podanych liczb to: {geometryczna}")

if not podano_zero:
    harmoniczna = i / suma_do_sr_harmonijnej
    print(f"Średnia harmoniczna podanych liczb to: {harmoniczna}")
