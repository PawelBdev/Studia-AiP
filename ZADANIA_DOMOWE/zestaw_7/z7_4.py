"""
Napisz funkcję o nagłówku
def co_drugi_znak(napis):
która zwróci napis zawierający co drugi znak z napisu napis podanego w parametrze.

"""

def co_drugi_znak(napis):
    licznik = 0
    nowy_napis = ""
    for n in napis:
        licznik += 1
        if licznik % 2 == 0:
            nowy_napis += n
    return nowy_napis


print(co_drugi_znak("rybak"))
print(co_drugi_znak("abcde"))
