'''
Napisz program, który pyta użytkownika o imię i nazwisko, następnie 
    wyświetla jego inicjały oraz 
    skleja imię i nazwisko w jeden napis ze spacją w środku (który to napis zostaje też wyświetlony). 
    Biorąc pod uwagę ostatnią literę imienia, wyświetla też płeć użytkownika (przyjmujemy, że płeć jest męska wtedy i tylko wtedy, gdy imię nie kończy się na 'a' lub 'A'). 
'''

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

print(imie[0] + "."+ nazwisko[0] + ".")
print(imie + " " + nazwisko) 

ostatnia = imie[-1]
if ostatnia.lower() != 'a':
    print("M")
else:
    print("K")
