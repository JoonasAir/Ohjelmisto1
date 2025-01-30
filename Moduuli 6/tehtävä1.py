import random

def noppa():
    return random.randint(1, 6)

luku = noppa()

while luku != 6:
    luku = noppa()
    print(f"Nopan silmäluku oli {luku}")
else:
    print("Luku oli 6, lopetetaan ohjelma")
