"""
pętla while - iteracja

while warunek:
    intrukcje, gdy warunek
    jest prawdziwy

przy while podajemy warunek wejścia w pętlę
"""

liczba = float(input("Liczba do spierwiastkowania: "))

while liczba < 0:
    print("Odmawiam")
    liczba = float(input("Liczba do spierwiastkowania: "))

# teraz już na pewno wiem, ze liczba jest nieujemna
print(f"pierw kwadr z {liczba} = {liczba**(1/2)}")

# to był przykład pętli zaporowej
