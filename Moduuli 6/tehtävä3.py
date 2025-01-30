def gallon(x):
    tulos = x * 3.785
    return tulos


maara = float(input("Syötä muutettavat gallonat: "))

y = gallon(maara)

while maara > 0:
    y = gallon(maara)
    print(f"{maara} gallonaa on yhteensä {y} litraa")
    maara = float(input("Syötä uudestaan muutettavat gallonat: "))
else:
    print("Syötit negatiivisen luvun, ohjelma lopetetaan")