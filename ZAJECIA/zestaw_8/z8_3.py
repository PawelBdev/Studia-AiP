'''
Napisz funkcję dokonującą klasyﬁkacji trójkątów ze względu na kąty.

Funkcja dla zadanych w trzech parametrach wejściowych alfa, beta, gamma miar w stopniach trzech kątów wewnętrznych w trójkącie, ma zwrócić (nie wyświetlić) rodzaj trójkąta:

    1 dla trójkąta prostokątnego,
    2 dla trójkąta rozwartokątnego,
    3 dla trójkąta ostrokątnego
    oraz 0 dla danych, które nie pozwolą utworzyć trójkąta. 
'''

def czy_katy_dodatnie(a, b, c):
    return True if (a > 0 and b > 0 and c > 0) else False 

def czy_poprawny_trojkat(a, b, c):
    return True if a + b + c == 180 else False

def max2(a, b):
    return a if a > b else b

def max3(a, b, c):
    x = max2(a, b)
    return max(x, c)

def ustal_rodzaj_trojkata(alfa, beta, gamma):
    if not (czy_katy_dodatnie(alfa, beta, gamma) and czy_poprawny_trojkat(alfa, beta, gamma)) :
        return 0
        
    najwiekszy_kat = max3(alfa, beta, gamma)
    if najwiekszy_kat == 90:
        return 1
    elif najwiekszy_kat > 90:
        return 2
    else:
        return 3
        

print(ustal_rodzaj_trojkata(-90, 90, 90)) # 0
print(ustal_rodzaj_trojkata(00, 90, 90)) # 0
print(ustal_rodzaj_trojkata(90, 45, 45)) # 1
print(ustal_rodzaj_trojkata(120, 30, 30)) # 2
print(ustal_rodzaj_trojkata(60, 60, 60)) # 3
