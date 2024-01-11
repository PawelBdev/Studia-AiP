"""
Napisz program służący do wyznaczania maksymalnej cyfry występującej w podanej liczbie całkowitej dodatniej.
Dane mają być pobrane od użytkownika (program ma wymuszać podanie liczby dodatniej),
zaś wynik działania należy wyświetlić na ekranie (wszystko z odpowiednimi komunikatami).
"""


while True:
    liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
    if liczba > 0:
        break

x = liczba 
cyfra_max = 1
while liczba > 0:
    i = liczba % 10
    if i > cyfra_max:
        cyfra_max = i
    liczba = liczba // 10

print(f"Maksymalna cyfra w liczbie {x} to {cyfra_max}.")
