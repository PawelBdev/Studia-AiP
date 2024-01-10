'''
Zdefiniuj funkcję o nagłówku
def znajdz_v1(napis, znak):
która zwraca indeks w napisie pierwszego od lewej wystąpienia elementu równemu podanemu znakowi. W przypadku nieznalezienia znaku zwracane jest -1. 
Zmodyfikuj nagłówek funkcji, aby domyślnie funkcja wyszukiwała pierwszego od lewej wystąpienia spacji.
'''

# v1 >>> rozwiazanie nieoptymalne
def znajdz_v1(napis, znak=" "):
    indeks = 0
    for el in napis:
        # print("indeks ", indeks)
        if el == znak:
            break
        indeks += 1
    if 0 <= indeks < len(napis):
        return indeks
    return - 1
    # return indeks if indeks >= 0 else -1
        
print("tatry, r", znajdz_v1("tatry", "r")) # 3
print("tatry, z", znajdz_v1("tatry", "z")) # -1
print("tatry, t", znajdz_v1("tatry", "t")) # 0
print("-" * 15)

# v2 >>> rozwiazanie prawidłowe
def znajdz_v2(napis, znak=" "):
    for i in range(len(napis)):
        if napis[i] == znak:
            return i
        return -1
    
print("tatry, r", znajdz_v2("tatry", "r"))
print("tatry, z", znajdz_v2("tatry", "z"))
print("tatry, t", znajdz_v2("tatry", "t"))
