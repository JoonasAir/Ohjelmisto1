luvut = []

luku = (input("Anna luku: "))

while luku != "":
    luvut.append(int(luku))
    luku = (input("Anna luku: "))

luvut.sort(reverse=True)

print(luvut[1:6])