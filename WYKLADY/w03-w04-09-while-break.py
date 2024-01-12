while True:
    liczba = int(input("podaj moją ulubioną liczbę: "))
    if liczba == 14: #warunek wyjścia z pętli
        print("Brawo!!!")
        break
print("Koniec gry")

#dodatkowe instrukcje sterujące przebiegiem programu
# break - przerywa wykonanie pętli
# w której jest zapisane - tylko jednej
# continue - przerywa wykonanie bieżącego obrotu pętli
# i idzie do sprawdzenia warunku

liczba = int(input("podaj moją ulubioną liczbę: "))
while liczba != 14:
    liczba = int(input("spróbuj jeszcze raz: "))
print("Brawo!!!")
print("Koniec gry")
    
