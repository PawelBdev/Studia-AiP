"""
Napisz program, który (po zapytaniu użytkownika o wysokość) wyświetla piramidę z gwiazdek, zbudowaną jak na przykładzie poniżej.
Przykład dla wysokości równej 4:
*
**
***
****
"""

i = 1
while i <= 4:
    print("*" * i)
    i += 1
