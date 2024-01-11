"""
Napisz program służący do wyznaczania lustrzanego odbicia liczby całkowitej dodatniej. Dane mają być pobrane od użytkownika (program ma wymuszać podanie liczby dodatniej), zaś wynik działania należy wyświetlić na ekranie (wszystko z odpowiednimi komunikatami).
"""

while True:
    liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
    if liczba > 0:
        break
lustrzane_odbicie = -liczba
print(f"Lustrzane odbicie liczby {liczba} to {lustrzane_odbicie}.")
