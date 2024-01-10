'''
Napisz program, który pobiera liczby podane przez użytkownika 
aż do momentu, gdy ich suma będzie większa niż 50. 
Na końcu 
    wyświetl tę sumę [oraz 
    liczbę pobranych danych [i 
    średnią arytmetyczną podanych danych]]. 
'''

suma = 0
i = 0

while suma < 50:
    liczba = float(input("Podaj liczbę: "))
    suma += liczba
    i += 1

print(f"suma = {suma}")
print(f"liczba pobranych danych = {i}")
print(f"średnia arytmetyczna pobranych danych = {suma / i}")

# To rozwiązanie na zajęciach było błędne. Powinno być:
"""
while suma <= 50:
"""
