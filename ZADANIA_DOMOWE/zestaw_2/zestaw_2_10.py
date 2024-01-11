"""
Jeden znaczek kosztuje 4 zł 50 gr.
Napisz program, który dla wprowadzonej przez użytkownika kwoty
poda ile znaczków można za nią kupić.
"""
cena_znaczka = 4.5

kwota = float(input("Podaj kwotę: "))

liczba_znacznow = kwota // cena_znaczka

print(liczba_znacznow)
