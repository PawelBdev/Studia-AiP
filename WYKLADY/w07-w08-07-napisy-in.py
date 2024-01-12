#sprawdzić czy znak jest w napisie
#sprawdzić czy element jest w sekwencji

#znak in napis
#napis1 in napis2

print("z" in "choinka")
print("a" in "choinka")
print("inka" in "choinka")
print("ala" in "choinka")

napis = "cho inka"
napis2 = ""
for znak in napis:
    if znak == " ":
        print("spacja")
    napis2 += znak * 3

print(napis)
print(napis2)
