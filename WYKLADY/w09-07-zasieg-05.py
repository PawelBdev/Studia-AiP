##zasięg zmiennych - miejsce, gdzie
##zmienna może zostać użyta
##zasięg globalny
##zasięg lokalny

def funkcja1():
    #w funkcji nie można w prosty sposób
    #modyfikować zmiennych globalnych
    global x #global informuje funkcję że zmienna jest globalna
    #NIE UŻYWAĆ
    x = x + 15 #modyfikacja zmiennej globalnej
    print("x w funkcji 1:", x)
    
# program
x = 5 #zmienna zadeklarowana w programie ma zasięg globalny
print("x w programie:", x) # 5
funkcja1() #20
print("x w programie:", x) # 20

"""
hermetyzacja - funkcje mają być odizolowane
i wzajemnie niezależne od siebie i programu głównego.
Komunikacja pomiędzy funkcjami a programem
ma odbywać się za pomocą parametrów.
"""
