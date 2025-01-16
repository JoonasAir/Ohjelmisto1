sex = input("Kerro biologinen sukupuolesi: ")
hgb = int(input("Syötä hemoglobiiniarvosi: "))

if 117<= hgb <=175 and sex == "nainen":
    print("Hemoglobiiniarvosi on normaali")
elif hgb > 175 and sex == "nainen":
    print("Hemoglobiiniarvosi on korkea")
elif hgb < 117 and sex == "nainen":
    print("Hemoglobiiniarvosi on alhainen")
elif 134<= hgb <=195 and sex == "mies":
    print("Hemoglobiiniarvosi on normaali")
elif hgb > 195 and sex == "mies":
    print("Hemoglobiiniarvosi on korkea")
elif hgb < 134 and sex == "mies":
    print("Hemoglobiiniarvosi on alhainen")
