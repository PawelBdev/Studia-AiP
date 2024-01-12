#napisy skadają się ze znaków
#znaki można porównywać

print("ola" > "ala") #True
print("Ola" > "ala") #False
print("a" == "a")
print("a" == "A")

#każdy znak ma swój numer
#porównywanie numerów znaków
#UNICODE

print("drzewo" > "ćma") #False - kod d jest wcześniejszy niż kod ć

print("" > "ala") #False
#napisz pusty jest wcześniejszy niż jakikolwiek napis

print(" " > "ala") #False

#ord(znak) - zwraca numer znaku dla jednego znaku
#chr(numer) - zwraca znak

print(ord("}"))
print(chr(289))


#print(ord("asd"))
#w Pythonie nie ma typu na pojedynczy znak

i = 257
while i < 300:
    print(chr(i), end = "   ")
    i += 1




