import random

kolme = ([random.randint (0, 9) for i in range (3)])
nelja = ([random.randint (1, 6) for i in range (4)])

print("Numerolukon kolmenumeroinen koodin on: ", *kolme)
print("Numerolukon nelinumeroinen koodi on: ", *nelja)

    



