"""
Napisz funkcję czy_jest_palindromem zwracającą odpowiedź (True lub False) na pytanie, czy napis zadany w argumencie jest palindromem.
czy_jest_palindromem('Ala') --> False
czy_jest_palindromem('ala') --> True
czy_jest_palindromem('') --> True
czy_jest_palindromem('kajak') --> True
czy_jest_palindromem('kobyła ma mały bok') --> False
czy_jest_palindromem('kobyłamamałybok') --> True
czy_jest_palindromem('anka') --> False
czy_jest_palindromem('anna') --> True
czy_jest_palindromem('ANNA') --> True
"""

def czy_jest_palindromem(napis):
    return True if napis == napis[::-1] else False


print(czy_jest_palindromem('Ala') == False)
print(czy_jest_palindromem('ala') == True)
print(czy_jest_palindromem('') == True)
print(czy_jest_palindromem('kajak') == True)
print(czy_jest_palindromem('kobyła ma mały bok') == False)
print(czy_jest_palindromem('kobyłamamałybok') == True)
print(czy_jest_palindromem('anka') == False)
print(czy_jest_palindromem('anna') == True)
print(czy_jest_palindromem('ANNA') == True)