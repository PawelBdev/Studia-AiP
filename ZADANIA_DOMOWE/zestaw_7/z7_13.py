"""
Rozwiązanie zadania umieść w jednym pliku:
Zdefiniuj funkcję logiczną
def czy_samogloska(znak):
która zwraca prawdę wtedy i tylko wtedy, gdy znak jest jedną z liter aeiouyąęAEIOUYĄĘ.
Wskazówka: aby sprawdzić czy jeden znak/napis jest znajduje się w drugim napisie można użyć in czyli znak in napis.

Napisz funkcję zwracającą napis złożony z samogłosek występujących na parzystych pozycjach napisu danego jako argument. Wykorzystaj funkcję czy_samogloska().

Napisz funkcję zwracającą napis złożony z co drugiej samogłoski napisu danego jako argument. Wykorzystaj funkcję czy_samogloska().
"""

def czy_samogloska(znak):
    return True if znak in "aeiouyąęAEIOUYĄĘ" else False


def zwroc_napis_z_samoglosek_na_parzystych(napis):
    licznik = 0
    nowy_napis = ""
    for n in napis:
        licznik += 1
        if licznik % 2 == 0 and czy_samogloska(n):
            nowy_napis += n
    return nowy_napis


def zwroc_napis_z_co_drugiej_samogloski(napis):
    licznik = 0
    nowy_napis = ""
    for n in napis:
        if czy_samogloska(n):
            licznik += 1
            if licznik % 2 == 0:
                nowy_napis += n
    return nowy_napis



# print(zwroc_napis_z_samoglosek_na_parzystych("To jest taki test"))
# print(zwroc_napis_z_samoglosek_na_parzystych("taka to ryba"))

print(zwroc_napis_z_co_drugiej_samogloski("Takatotohestanomaliayy."))