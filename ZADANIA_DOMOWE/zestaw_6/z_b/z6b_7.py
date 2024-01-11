''''
(*)Napisz program, który (po zapytaniu użytkownika o wysokość) wyświetla piramidę z gwiazdek, zbudowaną jak na przykładzie poniżej.
Przykład dla wysokości równej 4:

   *
  ***
 *****
*******
'''

n = int(input("Podaj wysokość piramidy: "))

i = 1
k = 1 
print("start")
while i <= n:
    print(f"{' ' * (n-i)} {'*' * k}")
    i += 1
    k += 2
