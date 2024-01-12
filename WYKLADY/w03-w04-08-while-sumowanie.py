#operacji redukcji

n = int(input("ile zsumować: "))
#akumulator
suma = 0
#element neutralny - nie zmienia wyniku działania
while n > 0:
    liczba = float(input("liczba: "))
    suma += liczba
    n -= 1
print(f"suma: {suma}")
