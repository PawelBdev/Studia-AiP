"""
Napisz funkcję o nagłówku
def usun(napis, znak):
która zwraca nowy napis równy staremu, ale pozbawiony wszystkich wystąpień znaku znak. Zmodyfikuj nagłówek funkcji, aby domyślnie funkcja usuwała z napisu spacje.
"""

def usun(napis, znak=" "):
    nowy_napis = ""
    for n in napis:
        if n != znak:
            nowy_napis += n
    return nowy_napis

print(usun("To jest test"))
print(usun("To jest test_2", "t"))