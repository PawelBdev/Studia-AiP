'''
Napisz program, który przyjmuje od użytkownika trzy liczby rzeczywiste będące długościami boków trójkąta, 
sprawdza, czy z podanych długości boków można zbudować trójkąt 
i wyświetla odpowiedni komunikat.

Ponadto, jeśli mogą tworzyć trójkąt, to 
    oblicza i wyświetla jego pole (ze wzoru Herona) 
    i obwód. 
Program wylicza wielkość pola tylko dla danych poprawnych, w przeciwnym wypadku wyświetla odpowiedni komunikat dla użytkownika. 

Warunki:

    Suma długości dwóch boków trójkąta jest zawsze większa od długości boku trzeciego
    p(p-a)(p-b)(p-c)>0
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
    print("trójkąt: ")
    print("pole: ", math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print("obwód: ", a+b+c)
else:
    print("nie można utworzyć trójkąta")