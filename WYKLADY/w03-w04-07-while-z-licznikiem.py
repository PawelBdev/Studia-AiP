pocz = int(input("od: "))
kon = int(input("do: "))
co_ile = int(input("co którą liczbę: "))

i = pocz
while i <= kon:
    print(f"{i} do kwadratu: {i**2}")
    i += co_ile
