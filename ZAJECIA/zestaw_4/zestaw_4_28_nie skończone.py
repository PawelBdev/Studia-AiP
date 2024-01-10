'''
Napisz program, który zapyta użytkownika o liczbę całkowitą n, po czym obliczy i wyświetli sumę 
1**1+2**2+3**3+…+n**n
'''

n = int(input("Podaj liczbę całkowitą : "))
i = 1
suma = 0
while i < n:
    print(i, end=", ")
    potega = i ** i
    print(i, potega)
    suma += potega
    i += 1
print(i)
print(suma)

# to jest nie skończone