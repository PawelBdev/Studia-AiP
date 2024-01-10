'''
Napisz program obliczający i wyświetlający
sumę n liczb wprowadzanych z klawiatury

(liczba n również pobrana od użytkownika).

Uwaga: dla n == 0 powinno wyjść zero.
'''

n = int(input("Podaj ilość liczb: "))
suma = 0
i = 1

while i <= n:
    liczba = float(input("Podaj liczbę: "))
    suma += liczba
    i += 1

print("Suma podanych liczb: ", suma)