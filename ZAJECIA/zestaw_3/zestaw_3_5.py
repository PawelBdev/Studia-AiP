'''
Napisz program, który pobiera od użytkownika współrzędne dwóch punktów w dwuwymiarowej przestrzeni euklidesowej.
Program ma napisać, czy dwa punkty się pokrywają 
(ale nie poprzez sprawdzanie długości [co może dać zły wynik!], lecz współrzędnych). 
Jeżeli punkty nie pokrywają się należy wyznaczyć oraz wyświetlić na ekranie długość odcinka utworzonego przez te punkty. 
'''
import math
# a_x1 = float(input("Podaj wsp x pkt A"))
# a_y1 = float(input("Podaj wsp y pkt A"))
# b_x1 = float(input("Podaj wsp x pkt B"))
# b_y1 = float(input("Podaj wsp x pkt B"))


x1 = 1
y1 = 0
x2 = 2
y2 = 0

if x1 == x2 and y1 == y2:
    print("Punkty pokrywają się")
else:
    # d = ((x1 - x2)**2 + (y1-y2)**2)**(1/2)
    d = math.sqrt((x1 - x2)**2 + (y1-y2)**2)
    print(f"Długość odcinka wynosi {d}")