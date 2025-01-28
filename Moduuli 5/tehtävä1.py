import random

maarat = []
i = 0

maara = int(input("Anna arpakuutioiden määrä: "))

while i < maara:
    noppa = random.randint(1, 6)
    maarat.append(noppa)
    i += 1

   
for tulos in maarat:
    print(tulos)    