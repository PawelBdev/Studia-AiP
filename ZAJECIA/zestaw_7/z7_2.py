'''
Napisz funkcję o nagłówku
def liczba_wystapien(napis, znak):
która zliczy i zwróci ile jest znaków znak w napisie napis podanym w parametrze.
Zmodyfikuj nagłówek funkcji, aby domyślnie funkcja zliczała wystąpienia znaku spacja.
'''

def liczba_wystapien(napis, znak=" "):
    wynik = 0
    for n in napis:
        if n == znak:
            wynik += 1
    return wynik
    

print(liczba_wystapien("chłopaki i dzewczyny", "i"), "chłopaki i dzewczyny".count("i"))
print(liczba_wystapien("chłopaki i dzewczyny"), "chłopaki i dzewczyny".count(" "))
print(liczba_wystapien("chłopaki i dzewczyny", "o"), "chłopaki i dzewczyny".count("o"))
print(liczba_wystapien("chłopaki i dzewczyny", "r"), "chłopaki i dzewczyny".count("r"))