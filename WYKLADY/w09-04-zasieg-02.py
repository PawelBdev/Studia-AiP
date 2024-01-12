##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    #funkcja MOŻE odczytywać wartość
    # zmiennych globalnych
    print("x w funkcji:", x)

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #5
print("x w programie:", x) #5
