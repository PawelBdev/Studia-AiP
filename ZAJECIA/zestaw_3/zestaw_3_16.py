'''
Napisz program, który dla podanego przez użytkownika roku w kalendarzu gregoriańskim
(który obowiązuje od 1582 roku), przekazuje informację o tym, 
czy jest to rok przestępny. 

Jeżeli rok nie spełnia warunku kalendarza gregoriańskiego program 
wyświetla odpowiedni komunikat i kończy pracę 
oraz nie podaje informacji o przestępności roku.

Wskazówka: rok jest przestępny, jeśli jego numer spełnia warunek: 

[jest podzielny przez 4 i nie jest podzielny przez 100] 
    lub 
[jest podzielny przez 400]. 
'''

rok = int(input("Podaj rok w kalendarzu gregoriańskim: "))
# rok = 1500

if rok < 1582:
    print("Rok nie spełnia warunku kalendarza gregoriańskiego. Koniec programu.")
else:
    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        print(f"Rok {rok} jest rokiem przestępnym")
    else:
        print(f"Rok {rok} nie jest rokiem przestępnym")