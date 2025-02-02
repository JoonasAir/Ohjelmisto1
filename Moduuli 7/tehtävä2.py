nimet = set()

kysynimi = input("Syötä nimi: ")

if kysynimi:
    nimet.add(kysynimi)
    print("Uusi nimi")

while kysynimi != "":
    kysynimi = input("Syötä nimi: ")
    if kysynimi == "":
        break
    if kysynimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(kysynimi)

print(nimet)
    