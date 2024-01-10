print("Zadanie 1")

a = 5
b = 10
c = 15
d = 20

print("a:", a**2 + b**2)
print("b:", (a + b) ** 2)
print("c:", a * b + c * d)
print("d:", (a - b) / (c + d))
print("e:", a / b * d)
print("f:", (a * b) / (c * d))
print("g:", a // 4)
print("h:", (a / b) ** 3)
print("i:", (abs(a - b)) ** 0.5)


print()
print("Zadanie 2")
h = 5
m = 40
s = 12

print((5 * 60 * 60) + 40 * 60 + 12)

print()
print("Zadanie 3")
s = 1000000
sek_w_dniu = 24 * 60 * 60
print(sek_w_dniu)
print(s // sek_w_dniu)

print()
print("Zadanie 4  -do domu")

print()
print("Zadanie 5")
print()

n = 459

jednosci = n % 10
n = n // 10
dziesiatki = n % 10
print("dziesiatki", dziesiatki)
print("jednosci", jednosci)

print()
print("Zadanie 6")
print()

dt = 0

print("dzien tyg: ", dt)
print("nasepny: ", (dt + 1) % 7)
print("poprzedni: ", (dt - 1) % 7)
