import numpy as np

T_val = np.array([24.8, 25.2, 25.2, 25.0, 25.0, 25.0, 25.0, 25.0, 24.9, 24.9])
nb_val = len(T_val)

mean = np.mean(T_val)
T_moins_mean = T_val - mean

sig = np.sqrt(1/(nb_val-1)*np.sum(T_moins_mean**2))

print(r'$\frac{1}{n}\sigma(T)$ = ', sig/np.sqrt(nb_val))
