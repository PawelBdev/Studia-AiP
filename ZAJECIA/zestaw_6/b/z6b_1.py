'''
Napisz program, który pobiera od użytkownika trzy znaki, a następnie na ekranie wypisuje wszystkie możliwe napisy 3-literowe jakie można utworzyć z tych znaków. Uwaga: Słowa nie muszą być sensowne. Użycie pętli jest niepotrzebne.
'''
a = input("Podaj znak 1: ")
b = input("Podaj znak 2: ")
c = input("Podaj znak 3: ")

print(a + b + c)
print(a + c + b)
print(b + a + c)
print(b + c + a)
print(c + a + b)
print(c + b + a)
