'''
Napisz program obliczający należny podatek dochodowy od osób fizycznych.

Program ma pobierać od użytkownika dochód 
i po obliczeniu wypisywać na ekranie należny podatek. 

Podatek obliczany jest według następujących reguł:

- do 120 000,00 PLN podatek wynosi 12% podstawy 
    minus kwota zmniejszająca podatek (3600 PLN), 
        przy czym uwaga: podatek nie może być ujemny!

- od 120 000,00 PLN podatek wynosi 10 800,00 PLN + 32% nadwyżki ponad 120 000,00 PLN.

'''

dochod = float(input("Podaj dochod: "))
# dochod = 100000

if dochod < 120000:
    podatek = dochod * 0.12
    if podatek - 3600 <= 0:
        print("Podatek wonosi 0 zł")
    else:
        print(f"Podatek wynosi {podatek - 3600}")
else:
    nadwyzka = dochod - 120000
    podatek_od_nadwyzki = nadwyzka * 0.32
    print(f"Podatek wynosi: {10800 + podatek_od_nadwyzki}")
