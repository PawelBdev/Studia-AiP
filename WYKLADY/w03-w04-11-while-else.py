"""
while warunek:
    instrukcje
else:
    wykonuje się gdy pętla zakończy się
    gdy warunek stanie się fałszywy
    czyli 'normalne' wyjście z pętli

else używa się z pętlą w której jest break
else wykonuje się wtedy, kiedy nie doszło
do użycia break
"""

haslo = "qwerty"
max_prob = 3
ile_razy = 0
while ile_razy < max_prob:
    proba = input("Podaj hasło: ")
    ile_razy += 1
    if proba == haslo:
        print("Zalogowano")
        break
    print("\nNiepoprawne hasło.")
else:
    print("\nZbyt wiele nieudanych prób.")
    print("Dostęp zablokowany")


