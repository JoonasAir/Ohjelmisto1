import random

i = 0
n = 0
N = int(input("Anna pisteiden määrä: "))

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        n += 1
    i += 1

lasku = 4*n/N
print(lasku)    






