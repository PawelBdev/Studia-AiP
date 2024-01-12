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
