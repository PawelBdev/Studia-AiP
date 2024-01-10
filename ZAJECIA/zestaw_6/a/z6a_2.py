'''
Rozwiązanie zadania umieść w jednym pliku:

    a. Napisz program (grę), który:
        losuje liczbę całkowitą od 1 do 100, ale jej nie podaje użytkownikowi;
        pobiera od użytkownika liczbę i porównuje ją z wylosowaną;
        jeśli są równe, to kończy działanie z komunikatem Gratulacje, zgadłeś!;
        jeśli nie, to pyta ponownie, poprzedzając pytanie komunikatem Podałeś za dużo! lub Podałeś za mało!

    b. Zmodyfikuj program z poprzedniego podpunktu, aby na końcu gry było wypisywane, w której próbie odgadujący zgadł liczbę.

    c. Zmodyfikuj program z poprzedniego zadania, aby umożliwiał wielokrotne przeprowadzenie gry. 
    W tym celu po zakończonej rozgrywce program ma pytać czy użytkownik chce ponownie zagrać udzielając odpowiedzi 
    tak (litery t/T) lub nie (litery n/N), inne znaki nie są akceptowane. 
'''

import random as r

def gra():  
    n = r.randint(1,100)
    print("\tDO TESTÓW: ", n)
    liczba = int(input("Zgadnij liczbę z zakresu od 1  do 100, którą wylosowałem: "))
    i = 1

    while n != liczba:
        if liczba < n:
            print("Za mało.")
        else:
            print("Za dużo.")
        liczba = int(input("Spróbuj ponownie: "))
        i += 1
    print(f"Gratulacje, zgadłeś w {i} próbie.")


# gra()

while True:
    gra()
    kontynuacja = input("Czy chcesz zagrać ponownie? Jeśli tak wybierz [t/T], jeśli nie wybierz [n/N]: ")
    print(f"kontynuacja: ", kontynuacja)
    
    while (kontynuacja.lower() != "n") and (kontynuacja.lower() != "t"):
        
        print("kontynuacja.lower(): ", kontynuacja.lower())
        
        kontynuacja = input("Wybierz [t/T], jeśli nie wybierz [n/N]")    
    
    if kontynuacja.lower() == "n":
        print("Program został zakończony.")
        break
    
    
    
    # W domu dokończyć pkt 2.c - nie działa prawidłowo