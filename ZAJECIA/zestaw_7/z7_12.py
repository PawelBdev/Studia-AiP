'''
Napisz funkcję liczba_wielkich_liter, która zwróci liczbę wielkich liter z alfabetu angielskiego występujących w napisie podanym w parametrze. 
'''

def liczba_wielkich_liter(napis):
    liczba = 0
    for znak in napis:
        if znak.isupper():
            liczba += 1
    return liczba
        

print(liczba_wielkich_liter("Koniec zajęć.")) # 1
print(liczba_wielkich_liter("Koniec DNIA.")) # 5