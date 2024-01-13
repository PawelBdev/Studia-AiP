"""
Szyfr Cezara polega na zastąpieniu każdej litery tekstu jawnego (niezaszyfrowanego) inną, oddaloną od niej o stałą liczbę pozycji w alfabecie (klucz). Cezar stosował przesunięcie o 3 miejsca w prawo.

Napisz funkcję, która zaszyfruje i zwróci podany w parametrze tekst szyfrem Cezara z kluczem podanym jako drugi parametr. Zakładamy, że klucz mieści się w zakresie. Domyślną wartością parametru odpowiadającego za przesunięcie niech będzie 3.
Napisz dwie wersje zadania:

Zakładamy, że w tekście występują jedynie wielkie litery alfabetu angielskiego oraz inne znaki. Litery są szyfrowane, a pozostałe znaki pozostają bez zmian.

Zakładamy, że w tekście występują litery alfabetu angielskiego (małe i wielkie) oraz inne znaki. Szyfrowanie zachowuje wielkość liter (tj. małe przechodzą na małe, a wielkie na wielkie), a pozostałe znaki pozostają bez zmian.

Jak odszyfrować zaszyfrowany tekst?
Wskazówka: szyfr Cezara jest szyfrem symetrycznym.
"""

# wersja 1 
def czy_z_alfabetu_ang_v1(znak):
    wartosc_liczbowa = ord(znak)
    return True if 65 <= wartosc_liczbowa <= 90 else False
    # return True if (65 <= wartosc_liczbowa <= 90 or 97 <= wartosc_liczbowa <= 122) else False


def szyfruj_tekst_v1(tekst, klucz=3):
    tekst_zaszyfrowany = ""

    for znak in tekst:
        if czy_z_alfabetu_ang_v1(znak):
            wartosc_liczbowa = ord(znak)
            if wartosc_liczbowa + klucz > 90:
                wartosc_liczbowa -= 26
            nowy_znak = chr(wartosc_liczbowa + klucz)
            tekst_zaszyfrowany += nowy_znak
        else:
            tekst_zaszyfrowany += znak

    return tekst_zaszyfrowany


print(szyfruj_tekst_v1("TO-JES-KOD:AB & Z"))
print(szyfruj_tekst_v1("TO-JES-KOD:AB & Z", 1))

# wersja 2
def czy_z_alfabetu_ang_v2(znak):
    wartosc_liczbowa = ord(znak)
    return True if (65 <= wartosc_liczbowa <= 90 or 97 <= wartosc_liczbowa <= 122) else False


def szyfruj_tekst_v2(tekst, klucz=3):
    tekst_zaszyfrowany = ""

    for znak in tekst:
        if czy_z_alfabetu_ang_v2(znak):
            wartosc_liczbowa = ord(znak)
            if wartosc_liczbowa in range(65, 91):
                if wartosc_liczbowa + klucz > 90:
                    wartosc_liczbowa -= 26
                nowy_znak = chr(wartosc_liczbowa + klucz)
            else:
                if wartosc_liczbowa + klucz > 122:
                    wartosc_liczbowa -= 26
                nowy_znak = chr(wartosc_liczbowa + klucz)

            tekst_zaszyfrowany += nowy_znak
        else:
            tekst_zaszyfrowany += znak

    return tekst_zaszyfrowany


test_szyfruj_v2 = szyfruj_tekst_v2("abc-ABC = XYZ & zyz")
print("tekst: abc-ABC = XYZ & zyz, zaszyfrowany: ", test_szyfruj_v2)


def odszyfruj_tekst_v2(tekst, klucz=3):
    tekst_odszyfrowany = ""

    for znak in tekst:
        if czy_z_alfabetu_ang_v2(znak):
            wartosc_liczbowa = ord(znak)
            if wartosc_liczbowa in range(65, 91):
                if wartosc_liczbowa - klucz < 65:
                    wartosc_liczbowa += 26
                nowy_znak = chr(wartosc_liczbowa - klucz)
            else:
                if wartosc_liczbowa - klucz < 97:
                    wartosc_liczbowa += 26
                nowy_znak = chr(wartosc_liczbowa - klucz)

            tekst_odszyfrowany += nowy_znak
        else:
            tekst_odszyfrowany += znak

    return tekst_odszyfrowany


tekst_odszyfruj_v2 = odszyfruj_tekst_v2(test_szyfruj_v2)
print("tekst:", test_szyfruj_v2, " odszyfroany: ", tekst_odszyfruj_v2)