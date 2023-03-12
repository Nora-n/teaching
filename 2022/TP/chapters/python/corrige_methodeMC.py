import numpy as np
N = 100000 # nombre de tirages

fprime = [] #initialisation liste vide
D = [54.3 , 54.9] #intervalle de D en cm (incertitude-type 3mm)
d = [26.5 , 27.1] #intervalle de d en cm (incertitude-type 3mm)

for i in range(N):
    Dtir = np.random.uniform(D[0], D[1])
    dtir = np.random.uniform(d[0], d[1])
    fprime.append((Dtir**2-dtir**2)/(4*Dtir))
    
# détermination du résultat de mesurage (arrondi)
fprime_mes = round(sum(fprime)/N,4)
fprime_inc = round(np.std(fprime,ddof=1),4)

#affichage
str_aff = "f' = " + str(fprime_mes) + ' +/- ' + str(fprime_inc) + ' cm'
print(str_aff)

