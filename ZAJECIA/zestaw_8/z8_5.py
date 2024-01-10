'''
Napisz funkcję, która otrzymuje w parametrze napis, 
zaś zwraca nowy napis utworzony z podanego, 
gdzie każda duża litera alfabetu angielskiego jest trzykrotnie powtórzona, 
pozostałe znaki pozostają bez zmian.

Np.:

    dla napisu "Kubus Puchatek" wynikiem będzie "KKKubus PPPuchatek"
    dla napisu "kotek" wynikiem będzie "kotek"
    dla napisu "ABECADŁO" wynikiem będzie "AAABBBEEECCCAAADDDŁOOO"
    dla napisu "W 80 dni dookoła świata!" wynikiem będzie "WWW 80 dni dookoła świata!" 
'''

def zwroc_nowy_napis(napis):
    nowy_napis = ''

    for znak in napis:
        if znak.isupper():
            nowy_napis += znak * 3
        else:
            nowy_napis += znak
    return nowy_napis


print(f"Kubus Puchatek \t {zwroc_nowy_napis('Kubus Puchatek')}")
print(f"ABECADŁO \t  {zwroc_nowy_napis('ABECADŁO')}")
print(f"W 80 dni dookoła świata! \t  {zwroc_nowy_napis('W 80 dni dookoła świata!')}")