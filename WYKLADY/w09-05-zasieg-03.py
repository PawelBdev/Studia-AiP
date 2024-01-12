##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    y = 115
    print("y w funkcji:", y)

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #115
print("y w programie:", y) #błąd
#zasięg globalny nie ma dostępu do zasięgu lokalnego
#nie można w programie korzystać ze zmiennych
#zadeklarowanych w funkcji
