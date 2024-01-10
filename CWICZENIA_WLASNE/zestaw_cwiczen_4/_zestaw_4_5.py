'''
Napisz program, który pobiera liczby podane przez użytkownika
aż do momentu, gdy ich suma będzie większa niż 50.
Na końcu
    wyświetl tę sumę [oraz liczbę pobranych danych
    [i średnią arytmetyczną podanych danych]].
'''

suma = 0
i = 0

while suma <= 50:
    n = float(input("Podaj liczbę: "))
    suma += n
    i += 1


print("Suma: ", suma)
print("Liczba pobranych danych: ", i)
print("Średnia arytmetyczna: ", suma / i)
