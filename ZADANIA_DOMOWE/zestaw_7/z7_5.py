"""
Napisz program, który pobiera od użytkownika napis oraz znak i wyświetla wszystkie znaki podanego napisu różne od podanego znaku.
"""

napis = input("Podaj napis: ")
znak = input("Podaj znak: ")

nowy_napis = ""

for n in napis:
    if n != znak:
        nowy_napis += n

print(nowy_napis)
