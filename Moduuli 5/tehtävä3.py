alku = True

luku = int( input("Anna kokonaisluku: ") )

for i in range(2, luku):
    if luku % i == 0:
        alku = False
        break

if (alku):
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")