import math

def laskin(koko, hinta):
    tulos = hinta / ((koko / 2) ** 2 * math.pi)
    return tulos

print("\nSyötä kahden eri pitsan tiedot laskeaksesi niille yksikköhinta euroina per neliömetri.")

koko1 = float(input("\nSyötä ensimmäisen pitsan halkaisija metreissä: "))
hinta1 = float(input("\nSyötä ensimmäisen pitsan hinta euroissa: "))

koko2 = float(input("\nSyötä toisen pitsan halkaisija metreissä: "))
hinta2 = float(input("\nSyötä toisen pitsan hinta euroissa: "))

tulos1 = laskin(koko1, hinta1)
tulos2 = laskin(koko2, hinta2)

if tulos1 < tulos2:
    print("\nEnsimmäisen pitsan hinnnalla saat enemmän vastinetta rahoillesi!")
else:
    print("\nToisen pitsan hinnalla saat enemmän vastinetta rahoillesi!")