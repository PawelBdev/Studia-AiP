'''
Napisz program, który pobierze od użytkownika liczbę całkowitą dodatnią n, a następnie wyświetli kwadrat z gwiazdek o rozmiarze n na n.
Uwaga: Użycie pętli jest niepotrzebne.
Przykład działania programu:
Podaj liczbę całkowitą dodatnią: 5
*****
*****
*****
*****
*****
'''
n = int(input("Podaj liczbę całkowitą dodatnią: "))

print((n * "*" + "\n") * (n - 1) + n * "*")

