L = [1, 2, 3]  # créé la liste L contenant les valeurs 1, 2 et 3
print(L[0])    # extrait la première valeur de L : 1
print(L[-1])   # extrait la dernière valeur de L : 3
print(L[:2])   # extrait les deux premières valeurs de L : 1 et 2
print(L[1:])   # extrait toutes les valeurs à partir de la deuxième : 2 et 3

L.append(42)    # ajoute l'élément 42 à la fin de la liste
L2 = L + [5, 6] # concatène la liste L et la liste [5, 6] dans une nouvelle
print(L2)       # [1, 2, 3, 42, 5, 6]
