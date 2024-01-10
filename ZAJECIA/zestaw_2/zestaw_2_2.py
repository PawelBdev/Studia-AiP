import datetime

imie = input("Podaj swoje imię: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))

obecny_rok = datetime.date.today().year
# obecny_rok = datetime.date.today().strftime("%Y")

wiek = obecny_rok - rok_urodzenia

print(f"{imie} masz {wiek} lat.")
