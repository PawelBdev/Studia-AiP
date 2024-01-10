'''
Napisz program wyznaczania wartości funkcji f(x) dla pobranego od użytkownika argumentu rzeczywistego
'''

x = float(input("podaj argument funkcji: "))

# x = 5

if x <= -1:
    w = x + 1
elif x <= 0:
    w = x**2 + (x+1)/(x+2)
else:
    w = x

print(f"f({x}) = {w}")