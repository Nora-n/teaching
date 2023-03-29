import numpy as np

T_val = np.array([25.3, 24.9, 25.1, 25.2, 23.8, 25.2, 25, 23, 24.9, 24.6, 25.1])
nb_val = len(T_val)
moy = np.mean(T_val)

# Calculs à la main avec numpy
T_moins_moy = T_val - moy
sig = np.sqrt(1/(nb_val)*np.sum(T_moins_moy**2))
print(f'sigma/sqrt(n) =  {sig/np.sqrt(nb_val)}')

# Calculs automatiques avec numpy
sig = np.std(T_val)
print(f'std/sqrt(n) = {sig/np.sqrt(nb_val)}')
