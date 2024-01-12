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
