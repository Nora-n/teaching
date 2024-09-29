for i in range(10):   # créé i qui commence à 0, terminera à 9, et augmente
                      # de 1 à chaque réalisation des lignes en-dessous
    print(i)          # affichera 0, puis 1, puis 2, et jusqu'à 9

L = []                # liste vide
for i in range(3):    # exécute la suite 3 fois : i=0, puis 1, puis 2
    L.append(3*i)     # ajoute 3*i à la fin de la liste
print(L)              # [0, 3, 6]

for i, k in enumerate(L):  # i compte à partir de 0, k prend les valeurs de L
    print(f'L[{i}] = {k}') # L[0] = 0, L[1] = 3, L[2] = 6

L2 = [3*i for i in range(3)] # créé L d'une manière plus compacte
print(L2)                    # même résultat
