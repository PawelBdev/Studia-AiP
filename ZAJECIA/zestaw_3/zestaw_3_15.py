'''
Napisz program, który przyjmuje od użytkownika trzy liczby rzeczywiste, 
sprawdza, czy mogą one być długościami boków trójkąta i wyświetla odpowiedni komunikat.

Ponadto, jeśli podane długości mogą tworzyć trójkąt, 
to wyświetla następujące informacje o tym trójkącie:

    Czy jest równoboczny?
    Czy jest równoramienny?
    Czy jest prostokątny? 
'''

import math

a = float(input("Podaj długość pierwszego boku trójkąta: "))
b = float(input("Podaj długość drugiego boku trójkąta: "))
c = float(input("Podaj długość trzeciego boku trójkąta: "))

# a = 2
# b = 2
# c = 2

p = (a+b+c)/2

if a+b>c and b+c>a and a+c>b and p*(p-a)*(p-b)*(p-c)>0:
    print("Trójkąt: ")
    if a == b == c:
        print("jest jest równoboczny")
    else:
        print("nie jest jest równoboczny")
        
    if a == b or b == c or a == c:
        print("jest jest równoramienny")
    else:
        print("nie jest jest równoramienny")
        
    if a**2 + b**2 == c**2 or \
        a**2 + c**2 == b**2 or \
        b**2 + c**2 == a**2:
        print("jest jest prostokątny")
    else:
        print("nie jest jest prostokątny")

else:
    print("nie można utworzyć trójkąta")