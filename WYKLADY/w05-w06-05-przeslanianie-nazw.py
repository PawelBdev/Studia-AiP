from math import cos

#tutaj jest wywołanie funkcji z modułu
print(cos(0.1))

#definicja tej funkcji przesłoni definicję
#cos() z modułu math
def cos(x):
    print(x**2)

#tutaj już wywołanie funkcji zdefiniowanej
cos(0.1)
