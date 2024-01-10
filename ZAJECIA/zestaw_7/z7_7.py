'''
Napisz program wczytujący z klawiatury jakiś napis,
a potem wypisujący go w dwóch linijkach: w pierwszej pierwsza połowa napisu, w drugiej druga połowa napisu. 
'''

napis = input("Podaj napis: ")

dl_napisu = len(napis)
print(napis[:dl_napisu // 2])
print(napis[dl_napisu // 2 : ])
