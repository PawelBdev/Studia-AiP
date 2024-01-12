##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    #każda zmienna zadeklarowana w funkcji
    # jest w jej zasięgu lokalnym
    x = 15
    print("x w funkcji:", x)

# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #15
print("x w programie:", x) #5
