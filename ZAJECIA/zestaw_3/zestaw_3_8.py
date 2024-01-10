'''
W firmie X miesięczna płaca podstawowa jest zwiększana m.in. o kwotę za przepracowane nadgodziny. 
Jeśli liczba nadgodzin przekroczy 30, to stawka za każdą kolejną nadgodzinę jest zwiększona o 50%. 

Napisz program, który dla wprowadzonej przez użytkownika liczby nadgodzin przepracowanych przez jednego pracownika 
oraz stawki za jedną nadgodzinę,
obliczy i wyświetli płacę za przeprowadzone nadgodziny. 
'''

godziny = int(input("Liczba godzin: "))
stawka = float(input("Stawka za godzinę: "))

if godziny <= 30:
    placa = godziny * stawka
    
else:
    placa = 30*stawka + (stawka - 30) * stawka * 1.5
    
print("Wynagrodzienie za nadgdziny: ", placa)