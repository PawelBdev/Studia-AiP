##int
##float
##bool
##str
##
##dynamicznie typowany

print(type(3))
print(type(3.5))
print(type(3>5))
print(type("ala"))

#silnie typowany
print(12 * 15)
print(12 * 3.5)
print("ala" * 3)
#print("ala" / 3)
#print("ala" * 3.5)

#każda nazwa typu jest funkcją konwersji
print(type(str(3)))
print(type(str(3.5)))
print(type(int(3>5)))
print(type(bool("ala")))
