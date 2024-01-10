'''
Śniadania w stołówce wydawane są w godzinach 7:45-11:30. 
Napisz program, który pobierze od użytkownika godzinę i minutę 
(zakładamy, że dane będą poprawne), a następnie wyświetli informację czy można o tej porze dostać śniadanie. 
'''

start_godz = 7
start_min = 45
koniec_godz = 11
koniec_min = 30

# godzina_od_uzytkownika = int(input("Podaj godzinę"))
# minuty_od_uzytkownika = int(input("Podaj minuty"))

g = 7
m = 45

if (start_godz < g < koniec_godz) or (g == start_godz and m >= start_min) or (g == koniec_godz and m <= koniec_min):  
    print("Mozesz dostać śniadanie")
else:
    print("Stołówka nie jest otwarta")

# v2 
# if 7*60+45 <= g*60+m <= 11*60+30:
#     print("Mozesz dostać śniadanie")
# else:
#     print("Stołówka nie jest otwarta")
