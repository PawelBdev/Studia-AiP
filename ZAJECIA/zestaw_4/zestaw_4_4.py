'''
Napisz program, który pobiera od użytkownika liczbę rzeczywistą 
i wyświetla jej kwadrat (czytelnie, z odpowiednim komunikatem), 
po czym całość (od momentu pobrania liczby włącznie!) się powtarza — 
i tak w kółko... 

Program kończy się, gdy podana liczba będzie zerem.

Zero kończące pobieranie nie podlega przetwarzaniu. 
'''

# v 1
# while True:
#     liczba = float(input("Podaj liczbę, zero kończy: "))
#     if liczba == 0:
#         break
#     print(f"Kwadrat liczby {liczba} wynosi {liczba ** 2}")
# print("Koniec.")

# v2
liczba = float(input("Podaj liczbę, zero kończy: "))

while liczba != 0:
    print(f"Kwadrat liczby {liczba} wynosi {liczba ** 2}")
    liczba = float(input("Podaj liczbę, zero kończy: "))
print("Koniec.")
