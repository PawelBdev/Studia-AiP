'''
Napisz funkcję o nagłówku
def rozne_znaki(napis, znak):
która zwróci napis zawierający wszystkie znaki napisu napis podanego w parametrze różne od podanego znaku.
'''

def rozne_znaki(napis, znak):
    nowy_napis = ""
    for n in napis:
        if n != znak:
            nowy_napis += n
    return nowy_napis


napis = input("Podaj napis: ")
znak = input("Podaj znak: ")

print(rozne_znaki(napis, znak))