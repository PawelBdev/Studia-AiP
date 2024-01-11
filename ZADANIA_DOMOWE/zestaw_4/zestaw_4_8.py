"""
Napisz program, który będzie wczytywał od użytkownika liczby całkowite aż do napotkania zera.
W trakcie pobierania program ma wyświetlać liczbę przeciwną dla każdej pobranej liczby
(czytelnie, z odpowiednim komunikatem).
Po zakończeniu pobierania należy wyświetlić ile było podanych liczb oraz iloczyn liczb przeciwnych.
Zero kończące wczytywany ciąg liczb nie jest jego elementem i nie należy go uwzględniać w obliczeniach.
"""

ilosc = 0
iloczyn_liczb_przecwnych = 1

while True:
    liczba = int(input("Podaj liczbę całkowitą. Podanie liczby zero konczy program. "))

    if liczba == 0:
        print("Podano liczbę zero. Koniec programu")
        break

    przeciwna = liczba * -1
    print(f"Podano liczbę {liczba}. Liczba przeciwna to {przeciwna}")
    iloczyn_liczb_przecwnych *= przeciwna
    ilosc += 1


if ilosc > 0:
    print(f"Ilość podanych liczb: {ilosc}")
    print(f"Iloczyn liczb przeciwnych: {iloczyn_liczb_przecwnych}")
else:
    print("Nie podano liczb do obliczeń.")
