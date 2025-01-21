hluokka = input("Kerro hyttiluokkasi (LUX, A, B tai C): ")

if hluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif hluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka!")