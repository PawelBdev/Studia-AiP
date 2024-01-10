'''
Napisz program, który będzie sprawdzał czy pobrana od użytkownika liczba całkowita jest:

parzysta czy nieparzysta,
podzielna przez 8. 
'''

liczba = int(input("Podaj liczbę: "))

if liczba % 2 == 0:
    print(f"Liczba {liczba} jest parzysta")
else:
    print(f"Liczba {liczba} jest nieparzysta parzysta")