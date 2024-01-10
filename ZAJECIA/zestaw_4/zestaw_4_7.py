'''
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią n
-- program mam wymuszać podanie liczby dodatniej 
    tzn. dopóki użytkownik podaje liczbę niedodatnią program informuje go o błędzie i każe wpisać ponownie. 
    
    Następnie program pobiera n liczb i na zakończenie wyświetla największą i najmniejszą z podanych liczb. 
'''

n = int(input("Podaj liczbę dodatnią: "))

while n <= 0:
    print(f"Liczba {n} nie jest dodatnia, spróbuj jeszcze raz")
    n = int(input("Podaj liczbę dodatnią: "))

liczba = float(input("Podaj liczbę: "))
liczba_min = liczba
liczba_max = liczba

while n > 1:
    n -= 1
    liczba = float(input("Podaj kolejną liczbę: "))

    if liczba > liczba_max:
        liczba_max = liczba

    if liczba < liczba_min:
        liczba_min = liczba
