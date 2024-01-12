#pętla for - uniwersalny iterator
#może przechodzić przez kolejne elementy
#sekwencji w uporządkowanej kolejności

##for licznik in zakres:
##    #przetwarzanie

##range(od, do, krok) - generuje liczby
## z zakresu <od, do) co krok - prawostronnie otwarty
##domyślnie: od = 0, krok = 1
##range(do)
##
##range - leniwy generator
# generuje kolejną liczbę dopiero wtedy kiedy jest
# potrzebna
print(range(10))

for i in range(10):
    print(i, end = "  ")
print()

for i in range(5, 200, 25):
    print(i, end = "  ")
print()

for i in range(1000, 200, -40):
    print(i, end = "  ")
print()

for i in range(10, 200, -40):
    print(i, end = "  ")
print()

for i in range(10, 20):
    print(i, end = "  ")
print()

napis = "choinka"
for i in range(len(napis)):
    print(napis[i])
