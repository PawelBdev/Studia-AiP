'''
Napisz program, który wyświetla co drugi znak z podanego przez użytkownika napisu. 
'''

napis = input("Podaj napis: ")

# v1
print("v1", napis[::2])
print()

# v2
i = 0
while i < len(napis):
    print("v2", napis[i])
    i += 2
print()

# v3 
for i in range(0, len(napis), 2):# skok co 2 elementy
    print("v3", napis[i])
