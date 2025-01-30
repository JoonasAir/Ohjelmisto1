def luvut(x):
    parittomat = []
    for i in x:
        if i % 2 != 0:
            parittomat.append(i)
    return parittomat

kluvut = [1, 2, 3, 4, 5, 6]

l = luvut(kluvut)

print(f"Lista parittomista luvuista: {l}")