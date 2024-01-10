'''
Napisz program, który będzie wczytywał od użytkownika liczby całkowite aż do napotkania zera. 
W trakcie pobierania program ma wyświetlać dla każdej pobranej liczby jej odwrotność 
(czytelnie, z odpowiednim komunikatem). 

Po zakończeniu pobierania należy wyświetlić 
    ile było podanych liczb oraz 
    sumę odwrotności pobranych liczb. 
Zero kończące wczytywany ciąg liczb nie jest jego elementem i nie należy go odwracać, zliczać ani sumować.
Uwaga: Liczba odwrotna do danej liczby x, to taka liczba y, że xy=1 (czyli liczbą odwrotną do x jest 1/x). 
'''

ilosc_liczb = 0
suma_odwrotnosci = 0
while True:
    liczba = int(input("Podaj liczbę całkowitą. Zero kończy. "))
    if liczba == 0:
        print("Koniec programu.")
        break
    odwrotnosc = 1 / liczba
    print(f"Odwrotnść liczby {liczba} to ", odwrotnosc)
    ilosc_liczb += 1
    suma_odwrotnosci += odwrotnosc

print(f"Podano {ilosc_liczb} liczb.")
print(f"Suma odwrotności pobranych liczb wynosi {suma_odwrotnosci}." )
