luku1 = int( input("Anna ensimmäinen kokonaisluku: "))
luku2 = int( input("Anna toinen kokonaisluku: "))
luku3 = int( input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print(f"Lukujen summa on: {summa}\nLukujen tulo on: {tulo}\nLukujen keskiarvo on: {keskiarvo:.2f}")