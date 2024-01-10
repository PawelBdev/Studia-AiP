''''
Napisz program, który losuje i wyświetla liczby całkowite ze zbioru {1, 2, 3, 4, 5, 6} aż do momentu wylosowania liczby 6, która również ma zostać wyświetlona.

'''
from random import randint

while True:
    wynik = randint(1, 6)
    print(wynik)
    if wynik == 6:
        break
