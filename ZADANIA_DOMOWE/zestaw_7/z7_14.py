"""
Napisz funkcję o nagłówku
def przeplec(napis, refren):
która zwraca nowy napis utworzony tak, jak w przykładach:

przeplec("napis", " ") --> "n a p i s"
przeplec("napis", ".") --> "n.a.p.i.s"
przeplec("", ".") --> ""
przeplec("napis", "**") --> "n**a**p**i**s"

"""

def przeplec(napis, refren):
    nowy_napis = ""
    for n in napis:
        nowy_napis += n + refren
    return nowy_napis


print(przeplec("napis", " "))
print(przeplec("napis", "."))
print(przeplec("", "."))
print(przeplec("napis", "**"))

