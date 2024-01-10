'''
Napisz program, który
    wczytuje z klawiatury liczbę,
    aż do chwili gdy będzie ona należała do przedziału <0,100).
'''
n = float(input("Podaj liczbę aż do chwili gdy będzie ona należała do przedziału <0,100): "))


# while not 100 > n >= 0:
while n < 0 or n >= 100:
    n = float(input("Podaj liczbę aż do chwili gdy będzie ona należała do przedziału <0,100): "))

print("POdana liczba to ", n)
