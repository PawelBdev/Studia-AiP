"""
Napisz program, który pobiera od użytkownika liczbę całkowitą dodatnią n (program ma wymuszać podanie liczby dodatniej), a następnie wyświetla wynik n rzutów monetą (dla każdego rzutu np. tekst postaci: 4. rzut -- wypadł orzeł). Po zakończeniu wszystkich rzutów program wyświetla podsumowanie, ile razy wśród n rzutów wypadł orzeł, a ile razy reszka. 
"""
import random as r


def orzel_reszka():
    liczba = r.randint(1, 2)
    if liczba == 1:
        wynik = "Wypadł orzeł"
    else:
        wynik = "Wypadła reszka"
    return wynik


while True:
    n = int(input("Podaj liczbę całkowitą dodatnią: "))
    if n > 0:
        break

i = 0
orly = 0
while n > 0:
    n -= 1
    wynik = orzel_reszka()
    if wynik == "Wypadł orzeł":
        orly += 1

    print(f"Rzut: {i} - {wynik}. ")
    i += 1

print(f"Liczba orłów: {orly}, ilość reszek: {i - orly}")
