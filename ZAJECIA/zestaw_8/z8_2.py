'''
Napisz program, który pyta użytkownika o dwie liczby całkowite i wyświetla kwadraty wszystkich liczb całkowitych pomiędzy nimi (włącznie z podanymi).
Należy zadbać o to, aby druga liczba była większa od pierwszej (pętla zaporowa). Przykład działania programu:
Podaj początek zakresu: 3
Podaj koniec zakresu: 1
Koniec nie może być mniejszy od początku. Podaj koniec jeszcze raz: 0
Koniec nie może być mniejszy od początku. Podaj koniec jeszcze raz: 6

3 do kwadratu = 9
4 do kwadratu = 16
5 do kwadratu = 25
6 do kwadratu = 36
'''

liczba_1 = int(input("Podaj początek zakresu: "))
liczba_2 = int(input("Podaj koniec zakresu: "))
while liczba_2 <= liczba_1:
    liczba_2 = int(input("Koniec nie może być mniejszy od początku. Podaj koniec jeszcze raz: "))
    
for i in range(liczba_1, liczba_2 + 1):
    print(f"kwadrat liczby {i} = {i ** 2}")
