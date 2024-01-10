"""
Napisz program, który pobierze od użytkownika pierwszą porę (godzinę i minuty). Jeżeli pora będzie poprawna program ma pobrać informację o drugiej porze. Jeżeli obie pory są poprawne, program ma wyświetlić informację o różnicy minut pomiędzy podanymi porami. W przypadku, gdy którakolwiek z pór nie będzie poprawna, program ma przerwać pracę, wydając użytkownikowi stosowny komunikat.
"""


def czy_poprawna_pora(g, m):
    godz_ok = False
    if 0 <= g < 24:
        godz_ok = True

    min_ok = False
    if 0 <= m < 60:
        min_ok = True

    return True if godz_ok and min_ok else False


def ile_minut(g, m):
    godziny_w_minutach = 0
    if g > 0:
        godziny_w_minutach = g * 60

    liczba_minut = godziny_w_minutach + m
    return liczba_minut


def roznica_por(g1, m1, g2, m2):
    ile_minut_1 = ile_minut(g1, m1)
    ile_minut_2 = ile_minut(g2, m2)

    if ile_minut_1 > ile_minut_2:
        wynik = ile_minut_1 - ile_minut_2
    elif ile_minut_1 < ile_minut_2:
        wynik = ile_minut_2 - ile_minut_1
    else:
        wynik = 0

    return wynik


print("Pierwsza pora...")
g1 = int(input("   podaj godzinę: "))
m1 = int(input("   podaj minuty: "))

if czy_poprawna_pora(g1, m1):
    print("Druga pora...")
    g2 = int(input("   podaj godzinę: "))
    m2 = int(input("   podaj minuty: "))

    if czy_poprawna_pora(g2, m2):
        print("Różnica minut pomiędzy porami: ", roznica_por(g1, m1, g2, m2))
    else:
        print("Druga pora podana niepoprawnie.")
else:
    print("Pierwsza pora podana niepoprawnie.")
