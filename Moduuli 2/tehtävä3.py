import math

kanta = float (input("Anna suorakulmion kanta:"))
korkeus = float(input("Anna suorakulmion korkeus:"))

pintaAla = kanta * korkeus
piiri = kanta + kanta + korkeus + korkeus

print(f"Suorakulmion pinta-ala on {pintaAla:.2f}")
print(f"Suorakulmion piiri on {piiri:.2f}")