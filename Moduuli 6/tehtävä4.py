def lista(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum

list = [1, 2, 3, 4, 5]

l = lista(list)

print(f"Listassa kokonaislukujen summa on yhteensä {l}")