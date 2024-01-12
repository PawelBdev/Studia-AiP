"""
Pobierz znak z klawiatury, wymuś, by była to litera alfabetu angielskiego (jeśli nie jest, to pytaj do skutku!), wypisz literę następną po podanej (przy czym po 'z' idzie 'a', a po 'Z' idzie 'A').

"""

def czy_litera_z_alfabetu_ang(znak):
    wartosc_liczbowa = ord(znak)
    return True if (65 <= wartosc_liczbowa <= 90 or 97 <= wartosc_liczbowa <= 122) else False


def nastepna_litera(znak):
    if znak == "z":
        return "a"
    elif znak == "Z":
        return "A"
    else:
        return chr(ord(znak) + 1)


while True:
    znak = input("Podaj literę z alfabetu angielskiego: ")
    if len(znak) == 1 and czy_litera_z_alfabetu_ang(znak):
            break
    else:
        znak = input("Podano nieprawidłową wartość. Podaj literę z alfabetu angielskiego: ")


print(f"Nowy znak: {nastepna_litera(znak)}" )
