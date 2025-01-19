luku = int(input("Anna vuosiluku: "))

if ((luku % 4 == 0 and luku % 100 != 0) or luku % 400 == 0):
    print("Vuosiluku on karkausvuosi")
else:
    print("Vuosiluku ei ole karkausvuosi")