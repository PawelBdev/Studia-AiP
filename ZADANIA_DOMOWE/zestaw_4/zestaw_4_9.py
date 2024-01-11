"""
Napisz program, który będzie wczytywał od użytkownika miary kątów w stopniach aż do napotkania zera
(zero kończy podawanie danych).

Dla każdej podanej miary kąta w stopniach program wyświetli miarę tego kąta w radianach
(czytelnie, z odpowiednim komunikatem).

Po zakończeniu pobierania należy wyświetlić
    ile było podanych miar kątów oraz
    ile wśród nich to były kąty ostre.

Zero kończące wczytywany ciąg miar kątów nie jest jego elementem i nie należy uwzględniać go w obliczeniach.
Zakładamy, że użytkownik będzie podawał kąty z przedziału <0∘,360∘>.
"""
from math import radians

ilosc = 0
ilosc_ostrych = 0
while True:
    podany_kat = float(input("Podaj miary kątów w stopniach. Zero kończy program. "))

    if podany_kat == 0:
        print("Koniec programu")
        break

    kat_w_radianach = radians(podany_kat)

    if podany_kat < 90:
        ilosc_ostrych += 1

    ilosc += 1
    print(f"Kąt {podany_kat} w radianach to {kat_w_radianach}")

if ilosc > 0:
    print(f'Ilość podanych miar kątów: {ilosc}')
    print(f'Ilość podanych kątów ostrych: {ilosc_ostrych}')
else:
    print("Nie podano żadnych kątów do obliczeń.")
