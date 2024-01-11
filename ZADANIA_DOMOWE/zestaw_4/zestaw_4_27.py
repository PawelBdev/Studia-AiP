"""
Napisz program, który pobierze od użytkownika ciąg liczb rzeczywistych różnych od zera.
Jeżeli użytkownik poda liczbę 0, to oznacza to koniec danych.

W trakcie pobierania program policzy sumę ujemnych wyrazów ciągu i iloczyn wyrazów dodatnich. Na ekran ma zostać wypisany komunikat:

Podanych liczb:_____, w tym
dodatnich:____,
ujemnych :____.

Suma liczb ujemnych:______.
Iloczyn liczb dodatnich:_______.

"""

i = 0
dodatnie = 0
ujemne = 0
suma_dodatnich = 0
iloczyn_ujemnych = 0

while True:
    n = float(input("Podaj liczbę rzeczywistą. Podanie zera kończy pobieranie danych: "))
    if n == 0:
        break

    i += 1
    if n > 0:
        dodatnie += 1
        suma_dodatnich += n

    if n < 0:
        ujemne += 1
        iloczyn_ujemnych *= n

print()
print(f'Podanych liczb: {i}, w tym')
print(f'dodatnich: {dodatnie},')
print(f'ujemnych: {ujemne}.')
print()
print(f'Suma liczb ujemnych: {suma_dodatnich}.')
print(f'Iloczyn liczb dodatnich: {iloczyn_ujemnych}.')
print()
