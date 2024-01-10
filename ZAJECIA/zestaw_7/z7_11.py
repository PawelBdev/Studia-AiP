'''
Napisz funkcję liczba_cyfr_w_napisie, która zwróci liczbę cyfr występujących w napisie podanym w parametrze.
liczba_cyfr_w_napisie('Ala ma 2 koty i 13 rybek.') --> 3
Wskazówka: znaki można porównywać np. sprawdzenie czy znak jest cyfrą można zapisać: znak >= '0' and znak <= '9'
'''

def liczba_cyfr_w_napisie_v1(napis):
    ilosc_cyfr = 0
    for znak in napis:
        if znak in "1234567890":
            ilosc_cyfr += 1
    return ilosc_cyfr

print("Ala ma 2 koty i 13 rybek.", liczba_cyfr_w_napisie_v1("Ala ma 2 koty i 13 rybek.")) # 3

def liczba_cyfr_w_napisie_v2(napis):
    ile = 0
    for znak in napis:
        if znak >= "0" and znak <= "9":
            ile += 1
    return ile

print("Ala ma 2 koty i 13 rybek.", liczba_cyfr_w_napisie_v2("Ala ma 2 koty i 13 rybek.")) # 3
        