'''
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią (program ma wymuszać podanie liczby dodatniej),
a następnie wyświetlający informację o tym, czy jest to liczba pierwsza. 
'''

while True:
    n = int(input("Podaj dodatnią: "))
    if n > 0:
        break
    
d = 1
suma_dzielnikow = 1

while d <= n//2:
    if n % d == 0:
        print(d)
        suma_dzielnikow += 1
    d += 1
# print(n)
# print("suma_dzielnikow: ", suma_dzielnikow)

if n == 2:
    print(f"Liczna {n} jest liczbą pierwszą") 
else: 
    print(f"Liczna {n} nie jest liczbą piwerszą")
