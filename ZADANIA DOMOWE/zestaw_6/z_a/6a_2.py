'''
Rozwiązanie zadania umieść w jednym pliku:
a) Napisz program (grę), który:
 - losuje liczbę całkowitą od 1 do 100, ale jej nie podaje użytkownikowi;
 - pobiera od użytkownika liczbę i porównuje ją z wylosowaną;
 - jeśli są równe, to kończy działanie z komunikatem Gratulacje, zgadłeś!;
 - jeśli nie, to pyta ponownie, poprzedzając pytanie komunikatem Podałeś za dużo! lub Podałeś za mało!

b) Zmodyfikuj program z poprzedniego podpunktu, aby na końcu gry było wypisywane, w której próbie odgadujący zgadł liczbę.

c) Zmodyfikuj program z poprzedniego zadania, aby umożliwiał wielokrotne przeprowadzenie gry.
W tym celu po zakończonej rozgrywce program ma pytać czy użytkownik chce ponownie zagrać udzielając odpowiedzi tak (litery t/T) lub nie (litery n/N), inne znaki nie są akceptowane.
'''

import random as r


def gra():
    liczba = r.randint(1, 100)
    print(f"liczba = {liczba}")
    proba = int(input("Zgadnij jaką wylosowałem liczbę: "))

    while True:
        if proba < liczba:
            proba = int(input("Podałeś za mało! Próbuj dalej: "))
        elif proba > liczba:
            proba = int(input("Podałeś za dużo! Próbuj dalej: "))
        else:
            print("Gratulacje, zgadłeś!")
            break


def gra_v2():
    liczba = r.randint(1, 100)
    print(f"liczba = {liczba}")
    proba = int(input("Zgadnij jaką wylosowałem liczbę: "))

    i = 1
    while True:
        if proba < liczba:
            proba = int(input("Podałeś za mało! Próbuj dalej: "))
        elif proba > liczba:
            proba = int(input("Podałeś za dużo! Próbuj dalej: "))
        else:
            print(f"Gratulacje, zgadłeśw {i} próbie!")
            break
        i += 1


while True:
    gra_v2()
    czy_dalej = input("Czy chcesz zagrać ponownie? Odpowiedz tak (litery t/T) lub nie (litery n/N): ")

    while czy_dalej.lower() not in ['t', 'n']:
        czy_dalej = input("Podano błędną odpowiedź. Odpowiedz tak (litery t/T) lub nie (litery n/N): ")

    if czy_dalej.lower() == 'n':
        print("Koniec gry.")
        break
