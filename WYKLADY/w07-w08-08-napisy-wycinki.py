napis = "dzisiaj jest zimny dzień"

#wycinki - slices
#napis[od:do:krok] - wycina fragment napisu <od, do)
#domyślnie od = 0, do = len(napis), krok = 1
#od i do są wymagane

print(napis)
print("napis[7]", napis[7])
print("napis[7:]", napis[7:])
print("napis[:]", napis[:])
print("napis[8:13]", napis[8:13])
print("napis[::2]", napis[::2])
print("napis[100:]", napis[100:]) #napis pusty
print("napis[::-1]", napis[::-1])
print("napis[0:len(napis):-1]", napis[0:len(napis):-1])
print("napis[6]", napis[6])

