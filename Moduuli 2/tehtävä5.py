leiviskat = float(input ("Anna leiviskät: "))
naulat = float(input ("Anna naulat: "))
luodit = float(input ("Anna luodit: "))

LUOTI_G = luodit * 13.3
NAULA_G = LUOTI_G * 32
LEIVISKAT_G = NAULA_G * 20

SUMMA_KG = int(LUOTI_G + NAULA_G + LEIVISKAT_G) / 1000
SUMMA_G = float(LUOTI_G + NAULA_G + LEIVISKAT_G) % 1000

print("Massa nykymittojen mukaan:")
print(f"{SUMMA_KG} kilogrammaa ja {SUMMA_G:.2f} grammaa.")