'''
(*) Napisz program, który próbuje zgadnąć liczbę, o której pomyślał użytkownik.

Na początku program prosi użytkownika, aby pomyślał liczbę od 1 do 100, którą trzeba odgadnąć.
Następnie komputer zaczyna zgadywać 
    -- po każdej jego próbie użytkownik musi określić, czy podana przez komputer liczba jest za duża, za mała czy może trafiona.

Wskazówka: Ustal, w jaki sposób użytkownik będzie komunikować komputerowi czy trafił, czy nie (np. m -- liczba za mała, d -- liczba za duża, t -- trafiona!).
'''

from random import randint


def podaj_liczbe_w_przedziale(a, z):
    return randint(a, z)


print("Pomyśl o liczbie od 1 do 100. Spróbuję ją odgadnąć.")

pocz = 1
kon = 100
while True:
    # print('--------------')
    # print(f"pocz = {pocz}; kon = {kon}")
    # print('--------------')

    liczba = podaj_liczbe_w_przedziale(pocz, kon)
    print(f"Zgaduję - czy Twoja liczba to {liczba}?")

    czy_zgadlem = input("Zgadłem? Wpisz 't' jeśli tak, jeśli nie wpisz lub dowolny inny znak:")

    if czy_zgadlem == 't':
        print("Koniec gry.")
        break
    else:
        nowy_zakres = input("Napisz 'm' jeśli moja liczba jest za mała lub dowolny inny znak jeśli była za duża: ")

    if nowy_zakres == "m":
        pocz = liczba + 1
    else:
        kon = liczba - 1
