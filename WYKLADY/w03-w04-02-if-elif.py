x = int(input("Podaj liczbę: "))
if x > 0:
    print("dodatnia")
else: #x <= 0
    if x == 0:
        print("zero")
    else:
        print("ujemna")
# selekcje mozna zagnieżdżać
#wcięcia się kumulują
if x > 0:
    print("dodatnia")
elif x == 0:
    print("zero")
#elif:
else:
    print("ujemna")

"""
Jeżeli mam if-elif-elif... to wykona się tylko jedna
gałąź selekcji. Pierwsza, dla której warunek będzie
prawdziwy.
"""
"""
Kolejność operatorów:
    1. operatory arytmetyczne
    2. operatory porównania
    3. spójniki logiczne: najpierw not, potem and,
    na końcu or.
Nawiasy zmieniają kolejność wykonywania.

2>3*6 or 4/2<5 and 2**5 != 4**3
2>6 or 2<5

Każda wartość różna od zera/pustej jest
interepretowana jako True:
- liczba różna od zera
- napis różny od pustego
- kolekcja (listy, krotki, słowniki) różna od pustej
Wartość None jest fałszywa.

Nie można porównywać wartości różnych typów.
Nie mają ustalonej definicji porządku.
"""
