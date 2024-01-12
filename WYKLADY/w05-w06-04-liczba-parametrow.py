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
