'''
Napisz program pobierający od użytkownika liczbę całkowitą dodatnią (program ma wymuszać podanie liczby dodatniej),
a następnie wyświetlający informację o tym, czy jest to liczba pierwsza.
'''
while True:
    n = int(input("Podaj dodatnią: "))
    if n > 0:
        break

i = 1
ile = 0
while i <= n // 2:
    if n % i == 0:
        ile += 1

    if ile == 2:
        break
    i += 1
if ile == 2:
    print(n, "nie jest liczbą pierwszą")
else:
    print(n, "jest liczbą pierwszą")
