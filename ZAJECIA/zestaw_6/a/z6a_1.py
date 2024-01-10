"""
Napisz program, który losuje i wyświetla liczby całkowite ze zbioru {1, 2, 3, 4, 5, 6}
aż do momentu wylosowania liczby 6, która również ma zostać wyświetlona. 
"""

import random as r

n = r.randint(1, 6)
print("liczba: ", n)

while n != 6:
    n = r.randint(1, 6)
    print("liczba: ", n)

# v2
while True:
    liczba = r.randint(1, 6)
    print(liczba)
    if liczba == 6:
        break

# v3
n = r.randint(1, 6)
while n != 6:
    print("liczba: ", n)
    n = r.randint(1, 6)
print("liczba: ", n)
