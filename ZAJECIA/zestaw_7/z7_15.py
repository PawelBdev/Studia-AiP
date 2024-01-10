'''
Napisz funkcję
def ukryj_tekst(tekst):
która zwróci napis ukrywający tekst.
Algorytm ukrywający tekst ma polegać na wstawieniu pomiędzy litery tego tekstu losowo wybranego znaku z alfabetu składającego się z samych samogłosek alfabetu łacińskiego (bez znaków diakrytycznych), czyli AEIOUY.
Na przykład dla napisu "KOMPUTER" wynikiem może być "KEOIMEPAUUTYEAR"
'''
import random 

#v 1 wersja nieopyalna
def ukryj_tekst_v1(tekst):
    nowy_napis = ""
    for i in range(len(tekst)-1):
        z = random.choice("aeiouy")
        nowy_napis += tekst[i]
        nowy_napis += z
        
    nowy_napis += tekst[i+1] 
    return nowy_napis
        
napis = "komputer"
print(ukryj_tekst_v1(napis))


# 2 ta wersja optymlna
def ukryj_tekst_v2(tekst):
    ukryty = ""
    for znak in tekst:
        ukryty += znak + random.choice("aeiouy")
    return ukryty[:-1]

napis = "komputer"
n = ukryj_tekst_v2(napis)
print(napis)
print(n)
print(n[::2])


    