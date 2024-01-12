napis = "choinka"
i = 0
while i < len(napis):
    print(i, "==>", napis[i])
    i += 1

#pozycje spacji
napis = "ala ma kota"
i = 0
while i < len(napis):
    if napis[i] == " ":
        print(i, end = "  ")
    i += 1

#zamiana znaku
i = 0
nowy_napis = ""
while i < len(napis):
    if napis[i] == " ":
        nowy_napis += "*"
    else:
        nowy_napis += napis[i]
    i += 1
print()
print(napis)
print(nowy_napis)

##w Pytnonie napisy są niemutowalne (nieedytowalne)
##- nie można wymienić w napisie pojedynczego znaku
## czyli nie można zrobić tak: napis[i] = "*" 
