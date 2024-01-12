"w03-w04-10-while-continue.py"
while True:
    liczba = int(input("podaj liczbę dodatnią, zero kończy: "))
    if liczba == 0: #warunek wyjścia z pętli
        break
    if liczba < 0:
        print("miała być dodatnia...")
        continue
    print("  .....przetwarzanie")
print("Koniec")


################################################## 

"w03-w04-08-while-sumowanie.py"
#operacji redukcji

n = int(input("ile zsumować: "))
#akumulator
suma = 0
#element neutralny - nie zmienia wyniku działania
while n > 0:
    liczba = float(input("liczba: "))
    suma += liczba
    n -= 1
print(f"suma: {suma}")


################################################## 

"w07-w08-03-napisy-porownywanie.py"
#napisy skadają się ze znaków
#znaki można porównywać

print("ola" > "ala") #True
print("Ola" > "ala") #False
print("a" == "a")
print("a" == "A")

#każdy znak ma swój numer
#porównywanie numerów znaków
#UNICODE

print("drzewo" > "ćma") #False - kod d jest wcześniejszy niż kod ć

print("" > "ala") #False
#napisz pusty jest wcześniejszy niż jakikolwiek napis

print(" " > "ala") #False

#ord(znak) - zwraca numer znaku dla jednego znaku
#chr(numer) - zwraca znak

print(ord("}"))
print(chr(289))


#print(ord("asd"))
#w Pythonie nie ma typu na pojedynczy znak

i = 257
while i < 300:
    print(chr(i), end = "   ")
    i += 1


################################################## 

"w05-w06-03-notatki-print.py"
##znaki specjalne np. Enter, tab
##mogę wprowadzić poprzedzająć \
##    \n, \t
##
##str + str ==> łączenie napisów
##str * int ==> powielanie napisu

print("ala", "ma", "kota", "i go lubi", "!",
      sep = "_")
i = 0
while i < 10:
    print("*" * i, end = " | ")
    i += 1


################################################## 

"w05-w06-09-parametry-nazwane.py"
def szlaczek2(znak, ile):
    print()
    print(znak * ile)
   
def main():
    #wywołanie z parametrami pozycyjnymi
    #pozycja parametru na liście parametrów
    #decyduje o jego roli
    #podane argumenty są przypisywane
    #kolejno do parametrów
    szlaczek2("*", 10)
    szlaczek2("@", 5)
    
    #wywołanie z parametrami nazwanymi
    #parametry są przypisywane do odpowiednich nazw
    szlaczek2(znak = "&", ile =  3)
    szlaczek2(znak = " ^.^ ", ile = 5)
    szlaczek2(ile =  3, znak = "&")
    szlaczek2(ile = 5, znak = " ^.^ " )

main()


################################################## 

"w03-w04-06-while-operatory.py"
#pętla z licznikiem

#liczniki i, j, k

n = 20
#preludium pętli
#instrukcje przygotowujące pętlę do działania
i = 1 #zainicjowanie licznika
while i < n:
    #refren pętli
    print(f"{i} do kwadratu: {i**2}")
    #w treści pętli musi znaleźć się
    #instrukcja, która spowoduje
    #że warunek będzie mógł stać się fałszywy
    i = i + 1 #aktualizacja licznika

"""
inkrementacja = zwiększenie o 1 ==> i = i + 1
dekrementacja = zmniejszenie o 1 ==> i = i -1

i = i + 1 ==> i += 1
Rozszerzone operatory przypisania:
    += -= *= /= **= %= //= ...
"""


################################################## 

"w07-w08-04-napisy-indeksowanie.py"
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


################################################## 

"w03-w04-04-while-zaporowa.py"
"""
pętla while - iteracja

while warunek:
    intrukcje, gdy warunek
    jest prawdziwy

przy while podajemy warunek wejścia w pętlę
"""

liczba = float(input("Liczba do spierwiastkowania: "))

while liczba < 0:
    print("Odmawiam")
    liczba = float(input("Liczba do spierwiastkowania: "))

# teraz już na pewno wiem, ze liczba jest nieujemna
print(f"pierw kwadr z {liczba} = {liczba**(1/2)}")

# to był przykład pętli zaporowej


################################################## 

"w09-05-zasieg-03.py"
##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    y = 115
    print("y w funkcji:", y)

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #115
print("y w programie:", y) #błąd
#zasięg globalny nie ma dostępu do zasięgu lokalnego
#nie można w programie korzystać ze zmiennych
#zadeklarowanych w funkcji


################################################## 

"w05-w06-10-parametry-domyslne.py"
#definicja funkcji z parametrami domyślnymi
def szlaczek(znak = "*", ile = 10):
    #print()
    print(znak * ile)

def main():
    #przy parametrach domyślnych decyduje kolejność
    szlaczek()
    szlaczek("*")
    szlaczek("@")
    szlaczek("&")
    szlaczek(" ^.^ ")
    szlaczek("*", 10)
    szlaczek("@", 5)
    szlaczek("&", 3)
    szlaczek(" ^.^ ", 5)
    #szlaczek(15)
    #można połączyć parametry domyślny z nazwanymi
    szlaczek(ile = 15)

main()


################################################## 

"w09-06-zasieg-04.py"
##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    x = 15
    print("x w funkcji 1:", x)
    y = 115
    print("y w funkcji 1:", y)    

def funkcja2():
    x = 25
    print("x w funkcji 2:", x)
    print("y w funkcji 2:", y)
    #funkcja nie może korzystać z zasiegu lokalnego
    #innej funkcji

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #15 115
funkcja2() #25 błąd


################################################## 

"w05-w06-05-przeslanianie-nazw.py"
from math import cos

#tutaj jest wywołanie funkcji z modułu
print(cos(0.1))

#definicja tej funkcji przesłoni definicję
#cos() z modułu math
def cos(x):
    print(x**2)

#tutaj już wywołanie funkcji zdefiniowanej
cos(0.1)


################################################## 

"w05-w06-06-return.py"
##w Pythonie każda funkcja coś zwraca
##co najwyżej może to być wartość None
##
##funkcja zwracająca wartość

def suma_od_0_do(ostatnia):
    i = 0
    suma = 0
    while i <= ostatnia:
        suma += i
        i += 1
    print("przed return")
    return suma
    print("po return")

##jeżeli funkcja ma przekazać jakąś wartość
##do punktu wywołania to należy użyć słowa
##return
##
##return kończy wykonywanie funkcji
## to znaczy, że nie wykonają się żadne instrukcje
## po wykonaniu return
##wszystkie zmienne utworzone w funkcji są usunięte

print(suma_od_0_do(10))
print(suma_od_0_do(20))


################################################## 

"w05-w06-04-liczba-parametrow.py"
#funkcja bezparametrowa
def szlaczek():
    print()
    print("*" * 20)
    print()

szlaczek()

##funkcja z parametrem
##nie określamy typu parametru
##jeżeli funkcja ma podany parametr w definicji
##to nie tworzymy go w funkji
def szlaczek(znak):
    print()
    print(znak * 20)

szlaczek("*")
szlaczek("@")
szlaczek("&")
szlaczek(" ^.^ ")

#parametry pozwalają na bardziej elastyczne,
#uniwersalne wykorzystanie funkcji

#funkcja z wieloma parametrami
def szlaczek(znak, ile):
    print()
    print(znak * ile)

szlaczek("*", 20)
szlaczek("@", 5)
szlaczek("&", -5)
szlaczek(" ^.^ ", 10)

##wywołując funkcję musi być zgodność co do liczby
## i typu argumentów w stosunku do parametrów

##nazwy funkcji mogą się przesłaniać
##szlaczek("!")


################################################## 

"w09-04-zasieg-02.py"
##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    #funkcja MOŻE odczytywać wartość
    # zmiennych globalnych
    print("x w funkcji:", x)

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #5
print("x w programie:", x) #5


################################################## 

"w07-w08-02-napisy-ograniczniki.py"
#tworzenie napisów

n1 = ''
n2 = ""
n3 = ''''''
n4 = """"""
print(n1, n2, n3, n4, sep = " & ")

n5 = 'H. Sienkiewicz "Potop"' #zagnieżdżanie ograniczników
n6 = "d'Artangnian"
n7 = '"kubuś puchatek" został napisany przez A.A. Milne\'a'

# znak specjalny \
#\n \t 
#nadaje specjalne specjalne znaczenie znakom
#odbiera specjalne znaczenie znakom
print(n5)
print(n6)
print(n7)

n8 = """wlazł
kotek
na
płotek"""
print(n8)

n9 = "c:\\temp\katalog"
print(n9)


################################################## 

"w03-w04-05-while-nieskonczona.py"
# while True:
#     print("*")

#pętla nieskończona
#CTRL+C - przerywa wykonanie programu w konsoli

# pętla nie wykona się ani razu


################################################## 

"w03-w04-02-if-elif.py"
x = int(input("Podaj liczbę: "))
if x > 0:
    print("dodatnia")
else: #x <= 0
    if x == 0:
        print("zero")
    else:
        print("ujemna")
# selekcje mozna zagnieżdżać
#wcięcia się kumulują
if x > 0:
    print("dodatnia")
elif x == 0:
    print("zero")
#elif:
else:
    print("ujemna")

"""
Jeżeli mam if-elif-elif... to wykona się tylko jedna
gałąź selekcji. Pierwsza, dla której warunek będzie
prawdziwy.
"""
"""
Kolejność operatorów:
    1. operatory arytmetyczne
    2. operatory porównania
    3. spójniki logiczne: najpierw not, potem and,
    na końcu or.
Nawiasy zmieniają kolejność wykonywania.

2>3*6 or 4/2<5 and 2**5 != 4**3
2>6 or 2<5

Każda wartość różna od zera/pustej jest
interepretowana jako True:
- liczba różna od zera
- napis różny od pustego
- kolekcja (listy, krotki, słowniki) różna od pustej
Wartość None jest fałszywa.

Nie można porównywać wartości różnych typów.
Nie mają ustalonej definicji porządku.
"""


################################################## 

"w07-w08-07-napisy-in.py"
#sprawdzić czy znak jest w napisie
#sprawdzić czy element jest w sekwencji

#znak in napis
#napis1 in napis2

print("z" in "choinka")
print("a" in "choinka")
print("inka" in "choinka")
print("ala" in "choinka")

napis = "cho inka"
napis2 = ""
for znak in napis:
    if znak == " ":
        print("spacja")
    napis2 += znak * 3

print(napis)
print(napis2)


################################################## 

"w05-w06-02-definiowanie-funkcji-zalety.py"
## jak napisać własną funkcję

##def nazwa_funkcji(lista_parametrow-formalnych):
##    tresc-funkcji

#szlaczek()
##nie można użyć funkcji przed jej zdefiniowaniem


##funkcja może nie mieć parametrów
## funkcja bezargumentowa
def szlaczek():
    print("\n*\t*\t********\n")

##zdefiniowanie funkcji to nie jest jej wywołanie
szlaczek()
szlaczek()
szlaczek()
szlaczek()
##
##Po co są funkcje?:
##    mniej pisania kodu, bez powtórzeń
##    możliwość wielokrotnego użycia
##    łatwiejsza modyfikacja kodu
##    łatwiejsze poprawianie błędów
##    łatwiejsze testowanie
##    podział na podzadania
##    przejrzystość kodu


################################################## 

"w09-03-zasieg-01.py"
##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    #każda zmienna zadeklarowana w funkcji
    # jest w jej zasięgu lokalnym
    x = 15
    print("x w funkcji:", x)

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #15
print("x w programie:", x) #5


################################################## 

"w03-w04-03-if-poprawne-dane.py"
liczba = float(input("Liczba do spierwiastkowania: "))

if liczba < 0:
    print("Odmawiam")
    liczba = float(input("Liczba do spierwiastkowania: "))

if liczba < 0:
    print("Odmawiam")
    liczba = float(input("Liczba do spierwiastkowania: "))

# i tak nie ma pewności, ze liczba jest nieujemna
print(f"pierw kwadr z {liczba} = {liczba**(1/2)}")


################################################## 

"w07-w08-06-for-range.py"
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


################################################## 

"w03-w04-11-while-else.py"
"""
while warunek:
    instrukcje
else:
    wykonuje się gdy pętla zakończy się
    gdy warunek stanie się fałszywy
    czyli 'normalne' wyjście z pętli

else używa się z pętlą w której jest break
else wykonuje się wtedy, kiedy nie doszło
do użycia break
"""

haslo = "qwerty"
max_prob = 3
ile_razy = 0
while ile_razy < max_prob:
    proba = input("Podaj hasło: ")
    ile_razy += 1
    if proba == haslo:
        print("Zalogowano")
        break
    print("\nNiepoprawne hasło.")
else:
    print("\nZbyt wiele nieudanych prób.")
    print("Dostęp zablokowany")


################################################## 

"w05-w06-01-wywolywanie-funkcji.py"
##Temat: podprogramy
##podprogram w Pythonie = funkcja
##funkcje standardowe
##np. print(), abs(), input(), math.sqrt()
##Użycie funkcji to wywołanie
##w nawiasie okrągłym podajemy parametry aktualne
## rozdzielone przecinkami
##nazwa_funkcji(arg1, arg2, arg3,...)
##aby wywołać funkcję trzeba znać jej specyfikację

##Funkcje mogą wyświetlać albo zwracać coś.

print("hello")
##jeżeli funkcja coś zwraca muszę "zaopiekować się"
## wynikiem
## albo wyświetlić albo podstawić pod zmienną
print(abs(-5))
x = abs(-4.16)
print(x)

#x = abs(-5, -4.16)
##ile podać argumentów? Zależy od  definicji funkcji

#x = abs("ala")
##typ argumentu musi być zgodny z podanym w definicji

print()
#może być wywołanie funkcji bez argumentów, o ile
# definicja na to pozwala

print("ala", x, "ma", "kota", "!!")

##używanie funkcji jest proste


################################################## 

"w05-w06-07-kolejnosc-w-programie.py"
##Konwencja
##kolejność elementów w programie:
##    importy
##    definicje funkcji
##    program właściwy

#importy
import math

#definicje funkcji
def szlaczek():
    print()
    print("*" * 20)
    print()

def szlaczek1(znak):
    print()
    print(znak * 20)

def szlaczek2(znak, ile):
    print()
    print(znak * ile)

def suma_od_0_do(ostatnia):
    i = 0
    suma = 0
    while i <= ostatnia:
        suma += i
        i += 1
    return suma

# program właściwy
szlaczek()
szlaczek1("*")
szlaczek1("@")
szlaczek1("&")
szlaczek1(" ^.^ ")
szlaczek2("*", 20)
szlaczek2("@", 5)
szlaczek2("&", -5)
szlaczek2(" ^.^ ", 10)
print(math.sqrt(16))
print("suma", suma_od_0_do(10))

##uporządkowanie programu pozwala uniknąć
##przesłaniania nazw


################################################## 

"w07-w08-01-napisy-wprowadzenie.py"
##int
##float
##bool
##str
##
##dynamicznie typowany

print(type(3))
print(type(3.5))
print(type(3>5))
print(type("ala"))

#silnie typowany
print(12 * 15)
print(12 * 3.5)
print("ala" * 3)
#print("ala" / 3)
#print("ala" * 3.5)

#każda nazwa typu jest funkcją konwersji
print(type(str(3)))
print(type(str(3.5)))
print(type(int(3>5)))
print(type(bool("ala")))


################################################## 

"w07-w08-08-napisy-wycinki.py"
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


################################################## 

"w03-w04-01-if.py"
"""
#selekcja - instrukcja wyboru
if warunek:
    instrukcje, które wykonają sie
    gdy warunek będzie prawdziwy
else:
    instrukcje, które wykonają się
    gdy warunek będzie fałszywy

dwukropek:
    wcięcie kodu - 4 spacje albo tab
    nie łączymy w jednym programie
    obu sposobów
"""

x = int(input("Podaj liczbę: "))
if x > 0:
    print("dodatnia")
else:
    print("niedodatnia")


################################################## 

"w05-w06-08-main.py"
##Konwencja
##kolejność elementów w programie:
##    importy
##    definicje funkcji
##    program właściwy

#importy
import math

#definicje funkcji
def szlaczek():
    print()
    print("*" * 20)
    print()

def szlaczek1(znak):
    print()
    print(znak * 20)

def szlaczek2(znak, ile):
    print()
    print(znak * ile)

def suma_od_0_do(ostatnia):
    i = 0
    suma = 0
    while i <= ostatnia:
        suma += i
        i += 1
    return suma

def main():
    szlaczek()
    szlaczek1("*")
    szlaczek1("@")
    szlaczek1("&")
    szlaczek1(" ^.^ ")
    szlaczek2("*", 20)
    szlaczek2("@", 5)
    szlaczek2("&", -5)
    szlaczek2(" ^.^ ", 10)
    print(math.sqrt(16))
    print("suma", suma_od_0_do(10))
    
# program właściwy
#powinien być jak najkrótszy i czytelny
main()

##uporządkowanie programu pozwala uniknąć
##przesłaniania nazw


################################################## 

"w07-w08-05-napisy-przetwarzanie.py"
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


################################################## 

"w03-w04-09-while-break.py"
while True:
    liczba = int(input("podaj moją ulubioną liczbę: "))
    if liczba == 14: #warunek wyjścia z pętli
        print("Brawo!!!")
        break
print("Koniec gry")

#dodatkowe instrukcje sterujące przebiegiem programu
# break - przerywa wykonanie pętli
# w której jest zapisane - tylko jednej
# continue - przerywa wykonanie bieżącego obrotu pętli
# i idzie do sprawdzenia warunku

liczba = int(input("podaj moją ulubioną liczbę: "))
while liczba != 14:
    liczba = int(input("spróbuj jeszcze raz: "))
print("Brawo!!!")
print("Koniec gry")


################################################## 

"w03-w04-07-while-z-licznikiem.py"
pocz = int(input("od: "))
kon = int(input("do: "))
co_ile = int(input("co którą liczbę: "))

i = pocz
while i <= kon:
    print(f"{i} do kwadratu: {i**2}")
    i += co_ile


################################################## 

"w09-02-rekurencja.py"
##Funkcje mogą wywoływać inne funkcje
##
##funkcje rekurencyjne
##funkcja która wywołuje samą siebie

def odliczanie(n):
    #wariant nierekursywny - wtedy kiedy
    # funkcja nie wywoła samej siebie
    if n < 1:
        print("START!!!")
    else: 
        print(n)
        odliczanie(n-1)

#każdą rekurencję można wyrazić za pomocą pętli
def odliczanie_iter(n):
    while n > 0:
        print(n)
        n -= 1
    print("START!!!")

#odliczanie(5000)
odliczanie_iter(5000)


################################################## 

"w09-01-testowanie.py"
# -*- coding: utf-8 -*-

# testowanie

def przeplec(napis, refren):
    if len(napis) != 0:
        nowy = ""
        for i in range(len(napis) - 1):
            nowy += napis[i] + refren
        return nowy + napis[-1]
    else:
        return ""

def test_przeplec ():
    print(przeplec("napis", " "))
    print(przeplec("napis", "."))
    print(przeplec("", "."))
    print(przeplec("napis", "**"))

    print(przeplec("napis", " ") == "n a p i s")
    print(przeplec("napis", ".") == "n.a.p.i.s")
    print(przeplec("", ".") == "")
    print(przeplec("napis", "**") == "n**a**p**i**s")

test_przeplec()


################################################## 

"w09-07-zasieg-05.py"
##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    #w funkcji nie można w prosty sposób
    #modyfikować zmiennych globalnych
    global x #global informuje funkcję że zmienna jest globalna
    #NIE UŻYWAĆ
    x = x + 15 #modyfikacja zmiennej globalnej
    print("x w funkcji 1:", x)
    
# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #20
print("x w programie:", x) # 20

"""
hermetyzacja - funkcje mają być odizolowane
i wzajemnie niezależne od siebie i programu głównego.
Komunikacja pomiędzy funkcjami a programem
ma odbywać się za pomocą parametrów.
"""

################################################## 