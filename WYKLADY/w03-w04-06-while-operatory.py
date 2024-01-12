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
