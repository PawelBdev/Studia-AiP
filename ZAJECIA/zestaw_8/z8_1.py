'''
Napisz program, który pobierze od użytkownika:

    spalanie samochodu (w litrach na 100 kilometrów),
    ilość paliwa w baku (w litrach),
    dystans do przejechania (w kilometrach).

Jeżeli wystarczy paliwa, to samochód przejeżdża tyle kilometrów ile zostało zadane przez użytkownika. 
Jeżeli nie wystarczy, to tyle ile się uda (samochód jedzie aż się skończy paliwo). Program wyświetla przejechaną odległość i ilość paliwa pozostałego w baku. 
Należy założyć, że spalanie jest stałe przez całą jazdę. 
'''
import math

spalanie_na_100 = float(input("Spalanie: "))
paliwo_w_litach = float(input("Paliwo: "))
dystans_w_km = float(input("Dystans: "))
      
mozliwy_dystans = (paliwo_w_litach / spalanie_na_100) * 100
# print("mozliwy_dystans", mozliwy_dystans)

if mozliwy_dystans >= dystans_w_km:
    print("Samochod przejedzie całą trasę. ")
else:
    print("Samochod przejedzie ", math.floor(mozliwy_dystans))


