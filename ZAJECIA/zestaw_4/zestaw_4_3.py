'''
Napisz program obliczający i wyświetlający 
sumę n liczb wprowadzanych z klawiatury 

(liczba n również pobrana od użytkownika).

Uwaga: dla n == 0 powinno wyjść zero. 
'''

n = int(input("Podaj ilość liczb do zsumowania: "))
suma = 0

while n > 0:
    liczba = float(input("Podaj liczbę: "))
    print(f"Podana liczba: {liczba}")
    suma += liczba
    n -= 1
    
print(f"Suma wynosi {suma}")
