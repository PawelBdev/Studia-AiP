'''
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią n
-- program mam wymuszać podanie liczby dodatniej
    tzn. dopóki użytkownik podaje liczbę niedodatnią program informuje go o błędzie i każe wpisać ponownie.

    Następnie program pobiera n liczb i na zakończenie wyświetla największą i najmniejszą z podanych liczb.
'''


n = int(input("liczbę całkowitą dodatnią: "))
while n <= 0:
    n = int(input("Podana liczna nie jest dodatnia. Podaj liczbę całkowitą dodatnią: "))

i = 1
liczba = float(input("Podaj liczbę: "))
najminiejsza = liczba
najwieksza = liczba

while i < n:
    if liczba > najwieksza:
        najwieksza = liczba

    if liczba < najminiejsza:
        najminiejsza = liczba

    liczba = float(input("Podaj liczbę: "))
    i += 1

print("najminiejsza: ", najminiejsza)
print("najwieksza: ", najwieksza)
