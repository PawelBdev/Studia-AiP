"""
Jeden bilet kosztuje 2 zł 30 gr. 
Napisz program, który pobierze liczbę biletów i poda koszt ich zakupu. 
"""
cena_biletu = 2.30

liczba_biletow = int(input("Ile chcesz kupic biletów? "))

wynik = cena_biletu * liczba_biletow

print("Łączny koszt biletów wynosi {:.2f}".format(wynik))