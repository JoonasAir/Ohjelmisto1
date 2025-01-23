import math

pieni = math.inf
iso = -math.inf

luku = input("Anna luku, tyhjä syöte lopettaa: ")

while luku != "":
    luku = float(luku)
    if luku <= pieni:
        pieni = luku
    elif luku >= iso:
        iso = luku
    luku = input("Anna luku, tyhjä syöte lopettaa: ") 

print (f"Pienin luku oli {pieni} ja isoin {iso}")
