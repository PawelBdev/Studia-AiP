'''
Napisz program, który (po zapytaniu użytkownika o wysokość) wyświetla piramidę z gwiazdek, zbudowaną jak na przykładzie poniżej.
Przykład dla wysokości równej 4:

*
 *
  *
   *
'''

n = int(input("Podaj wysokość piramidy: "))

i = 0
while i <= n:
    print(i * " " + "*")
    i += 1