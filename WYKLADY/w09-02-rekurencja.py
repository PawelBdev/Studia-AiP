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
