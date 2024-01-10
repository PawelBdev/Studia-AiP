"""
Napisz program wyświetlający sumę ostatnich czterech cyfr
pobranej od użytkownika dodatniej liczby całkowitej. 

Możesz założyć, że liczba ma zawsze cztery cyfry — jeżeli ma mniej, to brakujące są zerami. 
"""

liczba_wejsciowa = int(input("Podaj liczbę czterocyfrową: "))

# liczba_wejsciowa = 1123

liczba = liczba_wejsciowa

l_1 = liczba % 10 
liczba = liczba // 10
l_2 = liczba % 10
liczba = liczba // 10
l_3 = liczba % 10
liczba = liczba // 10
l_4 = liczba % 10

wynik = l_1 + l_2 + l_3 + l_4

print(f"Suma cyfr liczby {liczba_wejsciowa} to {wynik}.")