"""
Rozwiązanie zadania umieść w jednym pliku:
Napisz funkcję o nagłówku
def odwroc(napis):
która zwraca napis zapisany od końca.

Zdefiniuj funkcję o nagłówku
def wycinek(napis, pocz, kon):
która zwraca nowy napis utworzony ze znaków napisu danego, poczynając od znaku o indeksie pocz, a kończąc na znaku o indeksie kon.
wycinek('kotlet', 0, 2) == 'kot'
wycinek('kolacja', 1, 3) == 'ola'

Zdefiniuj funkcję o nagłówku
def szyfruj(napis, klucz):
która dla danego napisu zwróci ten sam napis zaszyfrowany prostym szyfrem odwracającym — klucz określa długość odwracanych fragmentów. Przykłady:
szyfruj("Aladyn", 2) --> "lAdany"
szyfruj("Aladyn", 3) --> "alAnyd"
szyfruj("Aladyn", 4) --> "dalAny"
szyfruj("Aladyn", 5) --> "ydalAn"
Wskazówka: skorzystaj z funkcji wycinek oraz odwroc (obie zdefiniowane wcześniej).

Zdefiniuj funkcję o nagłówku
def deszyfruj(napis, klucz):
która odwraca powyższy proces.
"""

def odwroc(napis):
    return napis[::-1]

def wycinek(napis, pocz, kon):
    return napis[pocz:kon + 1]

def wycinek_v2(napis, kon):
    return napis[:kon]

def szyfruj(napis, klucz):
    return odwroc(wycinek_v2(napis, klucz)) + napis[klucz:]

def deszyfruj(napis, klucz):
    return szyfruj(napis, klucz)


print(wycinek("kotlet", 0, 2))
print(wycinek("kolacja", 1, 3))
print("----------------")
print(wycinek_v2("Aladyn", 2))
print("----------------")
print(szyfruj("Aladyn", 2))
print(szyfruj("Aladyn", 3))
print(szyfruj("Aladyn", 4))
print(szyfruj("Aladyn", 5))
print("----------------")
print(deszyfruj("lAadyn", 2))
print(deszyfruj("ydalAn", 5))

