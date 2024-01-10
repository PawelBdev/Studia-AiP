# Program pobiera liczbę rzeczywistą oraz liczbę procent. Wyświetlany jest odpowiedni procent liczby. 

liczba = float(input("Podaj liczbę rzeczywistą: "))
procent = float(input("Podaj liczbę procentów: "))

wynik = liczba * procent / 100

print(f"Wynik: {wynik}")