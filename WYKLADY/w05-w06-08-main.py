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
