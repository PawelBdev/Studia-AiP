'''
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią 
    (program ma wymuszać podanie liczby nieujemnej),

a następnie wyświetlający na ekranie informację, 
ile cyfr ma podana liczba (wszystko z odpowiednimi komunikatami). 
'''

n = int(input("Podaj liczbę dodatnią: "))

while n <= 0:
    n = int(input("Liczba niepoprawna, podaj liczbę dodatnią: "))    
    
ile = 0
while n > 0:
    c = n % 10 #  wyznaczam ostatnią cyfrę liczby n
    # analizowanie cyfry
    
    ile += 1
    n = n // 10 # odrzucam ostatnią cyfrę liczby n

print(f"Liczba ma {ile} cyfr.")
