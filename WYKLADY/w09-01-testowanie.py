# -*- coding: utf-8 -*-

# testowanie

def przeplec(napis, refren):
    if len(napis) != 0:
        nowy = ""
        for i in range(len(napis) - 1):
            nowy += napis[i] + refren
        return nowy + napis[-1]
    else:
        return ""

def test_przeplec ():
    print(przeplec("napis", " "))
    print(przeplec("napis", "."))
    print(przeplec("", "."))
    print(przeplec("napis", "**"))

    print(przeplec("napis", " ") == "n a p i s")
    print(przeplec("napis", ".") == "n.a.p.i.s")
    print(przeplec("", ".") == "")
    print(przeplec("napis", "**") == "n**a**p**i**s")

test_przeplec()
