'''
Napisz program, który pobiera od użytkownika liczbę rzeczywistą
i wyświetla jej kwadrat (czytelnie, z odpowiednim komunikatem),
po czym całość (od momentu pobrania liczby włącznie!) się powtarza 
— i tak w kółko... 

Program kończy się, gdy podana liczba będzie zerem.

Zero kończące pobieranie nie podlega przetwarzaniu. 
'''

n = float(input("Podaj liczbę rzeczywistą, zero kończy program: "))

while n != 0:
    print(f"Kwartat liczby {n} wynosi {n ** 2}")
    n = float(input("Podaj liczbę rzeczywistą, zero kończy program: "))

print("Koniec.")