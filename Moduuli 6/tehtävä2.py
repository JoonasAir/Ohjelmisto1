import random

def noppa(maara):
    maara = random.randint(1, max)
    return maara

max = int(input("Anna nopan maksimisilmäluku: "))

luku = noppa(max)

while luku != max:
    luku = noppa(max)
    print(f"Heitettiin noppaa ja saatiin luku {luku}.")
else:
    print(f"Saatiin nopan maksimisilmäluku eli {max}, ohjelma lopetetaa.")