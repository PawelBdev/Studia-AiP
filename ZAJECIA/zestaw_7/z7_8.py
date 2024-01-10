'''
Napisz program, który wczytuje napis po czym wypisuje jego fragment od początku do pierwszego napotkanego znaku gwiazdki (włącznie). 
'''

napis = input("Podaj napis: ")

print("------ v1 ------")
nowy_napis = ""
i = 0
for n in napis:
    nowy_napis += n
    if n == "*":
        break
    
print(nowy_napis)

print("------ v2 ------ ")
indeks = napis.find("*")

if indeks >= 0:
    print(napis[:indeks + 1])
else:
    print(napis)