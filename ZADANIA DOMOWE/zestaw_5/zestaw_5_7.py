"""
Napisz program, który będzie pobierał od użytkownika dwie liczby naturalne i zwracał odpowiedź na pytanie, czy podane liczby są względnie pierwsze.
W tym celu:
    napisz funkcję, która wyznaczy największy wspólny dzielnik dwóch liczb -- algorytm Euklidesa;
    napisz funkcję, która udzieli odpowiedzi na pytanie, czy dane dwie liczby naturalne są względnie pierwsze (wykorzystaj funkcję wyznaczającą największy wspólny dzielnik!).
"""


def zwroc_nwd_2_liczb(a, b):
    while b:
        a, b = b, a % b
    return a


def ustal_czy_sa_wzglednie_pierwsze(a, b):
    wynik = zwroc_nwd_2_liczb(a, b)
    return True if wynik == 1 else False


x = int(input("Podaj piewrszą liczbę naturalną: "))
y = int(input("Podaj drugą liczbę naturalną: "))

czy_liczby_wzglednie_pierwsze = ustal_czy_sa_wzglednie_pierwsze(x, y)

if czy_liczby_wzglednie_pierwsze:
    odp = "są"
else:
    odp = "nie są"

print(f"Podane liczby {x} i {y} {odp} względnie pierwsze.")
