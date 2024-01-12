##napis - typ złożony
##jest dostęp do poszczególnych składowych
##dostęp do poszczególnych
##napisy należą do sekwencji w Pythonie:
##    napisy, krotki, listy, słowniki

#długość napisu - len(napis)
n = "ala ma kota"
print(len(n))

print(len("")) #0
print(len("c:\\temp\\aip")) #11
print(len("a\nb\nc")) #5

#dostęp do poszczególnych znaków
#indeksowanie - dostęp do składowej o podanym numerze
# zmienna[nr]

##len("grudzień") == 8
##g|r|u|d|z|i|e|ń
##0|1|2|3|4|5|6|7
##-8|-7|-6|-5|-4|-3|-2|-1
##
##ostatni znak: napis[len(napis) - 1] albo napis[-1]

n = "plecak"
print(n[len(n)-1], n[-1]) #ostatnia
print(n[0], n[-len(n)]) #pierwsza

print(n[len(n)])
#jeżeli indeks wykracza poza zakres to jest
# wyjątek IndexError





