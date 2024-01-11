"""
Napisz program, który wczytuje napis po czym wypisuje jego fragment od pierwszego znaku gwiazdki do końca.
"""

napis = input("Podaj napis: ")

pozycja_gwiazdki = napis.find("*")

print(napis[pozycja_gwiazdki:])