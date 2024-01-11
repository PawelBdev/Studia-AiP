"""
Napisz program, który wczytuje z klawiatury napis, a następnie zlicza i wyświetla liczbę wystąpień w nim litery a.
"""

wyraz = input("Wpisz tekst, zliczę w nim ilość wystąpień litery 'a': ")

ile = wyraz.lower().count("a")
print(f"Liczba wystąpień litery a: {ile}")