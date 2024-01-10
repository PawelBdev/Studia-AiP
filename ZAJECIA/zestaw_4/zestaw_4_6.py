'''
Napisz program, który 
    wczytuje z klawiatury liczbę, 
    aż do chwili gdy będzie ona należała do przedziału <0,100). 
'''

# To przykład pętli zaporowej

# v1
# while True:
#     liczba = float(input("Podaj liczbę, aż do chwili gdy będzie ona należała do przedziału <0,100): "))
#     if 100 > liczba >= 0:
#         print(f"Podałeś {liczba}") 
#         break

# print(f"Koniec programu.")    
    
    
# v2 
liczba = float(input("Podaj liczbę, aż do chwili gdy będzie ona należała do przedziału <0,100): "))
while liczba < 0 or liczba >= 100:
    liczba = float(input("Podaj liczbę, aż do chwili gdy będzie ona należała do przedziału <0,100): "))