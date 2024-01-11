"""
Napisz program, który pobiera współrzędne dwóch punktów
(zakładamy, że różnych) w przestrzeni euklidesowej dwuwymiarowej,
a następnie wyznacza długość odcinka utworzonego przez te punkty
oraz wyświetla równanie prostej przechodzącej przez te dwa punkty.
"""

print("Podaj współrzędne punktów, dla któwych ma być wyznaczona długość odcinka.")

x1 = float(input("Podaj współrzędną X pierwszego punktu: "))
y1 = float(input("Podaj współrzędną Y pierwszego punktu: "))
x2 = float(input("Podaj współrzędną X drugiego punktu: "))
y2 = float(input("Podaj współrzędną X drugiego punktu: "))

d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)

d_zaokraglone = round(d, 2)

print(f"Długość odcinka dla punktów ({x1}, {y1}) i ({x2}, {y2}) wynosi {d_zaokraglone}")
