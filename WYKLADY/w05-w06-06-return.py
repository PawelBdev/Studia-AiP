##w Pythonie każda funkcja coś zwraca
##co najwyżej może to być wartość None
##
##funkcja zwracająca wartość

def suma_od_0_do(ostatnia):
    i = 0
    suma = 0
    while i <= ostatnia:
        suma += i
        i += 1
    print("przed return")
    return suma
    print("po return")

##jeżeli funkcja ma przekazać jakąś wartość
##do punktu wywołania to należy użyć słowa
##return
##
##return kończy wykonywanie funkcji
## to znaczy, że nie wykonają się żadne instrukcje
## po wykonaniu return
##wszystkie zmienne utworzone w funkcji są usunięte

print(suma_od_0_do(10))
print(suma_od_0_do(20))
