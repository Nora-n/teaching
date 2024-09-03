def puissance(arg1, arg2): # définit la fonction puissance de 2 arguments
    resultat = arg1**arg2  # variable locale de calcul
    return(resultat)       # fin de la fonction, résultat final

print(puissance(2, 3))     # donne le résultat du calcul : 8

def comparaison(x,y):
    if x > y:                                    # condition d'exécution
        print("argument 1 supérieur au second")  # si oui, exécute
    elif x < y:                                  # sinon, autre condition
        print("argument 1 inférieur au second")  # si oui, exécute
    else:                                        # pour tous les autres cas,
        print("argument 1 égal au second")       # exécute

print(comparaison(1,2))    # "argument 1 inférieur au second"
