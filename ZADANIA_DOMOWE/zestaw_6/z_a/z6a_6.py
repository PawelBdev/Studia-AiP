'''
Rozwiązanie zadania umieść w jednym pliku:
a. Napisz funkcję o nagłówku:
    def rzut_koscia(s):
która symuluje i zwraca rzut (liczbę oczek) jedną kością s -ścienną
(czyli kością o s ścianach ponumerowanych od 1 do s).
Zmodyfikuj nagłówek funkcji, aby domyślnie symulowany był rzut kością 6-ścienną.

b. Napisz funkcję o nagłówku:
    def rzut_koscia_p(s):
która symuluje i zwraca rzut jedną kością s-ścienną premiową. 
Kość premiowa to taka, której maksymalny wynik rzutu skutkuje powtórzeniem rzutu (dorzutem),
przy czym dodatkowy rzut także jest premiowy; 
ostateczny wynik rzutu kością premiową to suma wyników wszystkich wykonanych rzutów.

c. Napisz funkcję o nagłówku:
    def rzut_koscmi(k, s):
która symuluje i zwraca sumę rzutów (sumę oczek) k kośćmi s-ściennymi.

d. Napisz funkcję o nagłówku:
    def rzut_koscmi_p(k, s):
która symuluje i zwraca sumę rzutów (sumę oczek) k kośćmi s-ściennymi premiowymi.

Dodatkowo należy napisać funkcję def test():, która testuje każdą z napisanych funkcji w kilku różnych przypadkach i wyniki czytelnie wyświetla.
'''

from random import randint


def rzut_koscia(s=6):
    return randint(1, s,)


def rzut_koscia_p(s):
    wynik = 0
    rzut = randint(1, s)
    # print("pierwszy rzut = ", rzut)
    wynik += rzut
    while rzut == s:
        rzut = randint(1, s)
        # print("kolejny rzut = ", rzut)
        wynik += rzut
    return wynik


def rzut_koscmi(k, s=6):
    wynik = 0
    while k > 0:
        rzut = rzut_koscia(s)
        # print("rzut", rzut)
        wynik += rzut
        k -= 1
    return wynik


def rzut_koscmi_p(k, s):
    wynik = 0
    while k > 0:
        rzut = rzut_koscia_p(s)
        wynik += rzut
        k -= 1
    return wynik


def test():
    print("-" * 50)
    print("Test funkcji rzut_koscia(s). Wynik = ", rzut_koscia())
    print("-" * 50)
    print("Test funkcji rzut_koscia_(s). Wynik = ", rzut_koscia_p(6))
    print("-" * 50)
    print("Test funkcji rzut_koscia_(s). Wynik = ", rzut_koscia_p(6))
    print("-" * 50)
    print("Test funkcji rzut_koscmi(k, s). Wynik = ", rzut_koscmi(2, 6))
    print("-" * 50)
    print("Test funkcji rzut_koscmi_p(k, s). Wynik = ", rzut_koscmi_p(2, 6))
    print("-" * 50)


test()
