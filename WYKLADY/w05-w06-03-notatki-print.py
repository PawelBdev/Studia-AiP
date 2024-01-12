##znaki specjalne np. Enter, tab
##mogę wprowadzić poprzedzająć \
##    \n, \t
##
##str + str ==> łączenie napisów
##str * int ==> powielanie napisu

print("ala", "ma", "kota", "i go lubi", "!",
      sep = "_")
i = 0
while i < 10:
    print("*" * i, end = " | ")
    i += 1
