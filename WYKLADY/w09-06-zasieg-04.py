##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    x = 15
    print("x w funkcji 1:", x)
    y = 115
    print("y w funkcji 1:", y)    

def funkcja2():
    x = 25
    print("x w funkcji 2:", x)
    print("y w funkcji 2:", y)
    #funkcja nie może korzystać z zasiegu lokalnego
    #innej funkcji

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #15 115
funkcja2() #25 błąd

