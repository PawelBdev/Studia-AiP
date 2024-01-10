'''
Napisz program znajdowania iloczynu dwóch niepustych zbiorów, przy założeniu, że zbiory są reprezentowane jako domknięte przedziały liczb rzeczywistych tj. A=[a1, a2], B=[b1, b2].

Dane:
a1, a2 - parametry rzeczywiste oznaczające początek i koniec przedziału A;
b1, b2 - parametry rzeczywiste oznaczające początek i koniec przedziału B

Wyniki:
Na ekranie wyświetlane są alternatywnie informacje o tym, że iloczyn zbiorów jest zbiorem pustym lub o tym, że iloczyn zbiorów nie jest zbiorem pustym wraz z dwiema liczbami rzeczywistymi p1, p2 (początek i koniec iloczynu).

Operacje pomocnicze zrealizuj za pomocą funkcji.
Wskazówka: Można skorzystać z funkcji min(). 
'''

a_pocz = 15
a_kon = 25

b_pocz = 5
b_kon = 30

zbior_pocz = max(a_pocz, b_pocz)
zbior_kon = min(a_kon, b_kon)
print("zbior_pocz", zbior_pocz)
print("zbior_kon", zbior_kon)

if zbior_pocz < zbior_kon:
    print(f"Iloczyn zbiorów nie jest zbiorem pustym. \nPoczątek iloczynu {zbior_pocz}, koniec iloczynu {zbior_kon}.")
else:
    print(f"Iloczyn zbiorów jest zbiorem pustym.")
    
# ! przetestowac na innych przykładach
