import random

luku = random.randint(1,10)

arvaus = int(input("Arvaa oikea luku 1-10 välillä: "))

while arvaus != luku:
    if arvaus < luku:
        print("Arvaus oli liian pieni!")
    elif arvaus > luku:
        print("Arvaus oli liian suuri!")
    arvaus = int(input("Arvaa oikea luku 1-10 välillä: "))

print(f"Oikein! Luku oli {luku}")

