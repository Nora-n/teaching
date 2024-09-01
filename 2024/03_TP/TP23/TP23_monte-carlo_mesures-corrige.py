# Disponible sur Capytale avec le code 4186-1558000

import numpy as np

# =========================================================================== #
#                              Incertitudes                                   #
# =========================================================================== #

f = 100         # dilution par 100
uf = 1e-2*f     # uf/f = 1%
C2 = 1e-2       # mol.L^-1
uC2 = 1e-2*C2   # uC2/C2 = 1%
V1 = 10e-3      # L
uV1 = 0.02e-3   # L
Veq = 11.75e-3  # L
uVeq = 0.1e-2   # L

C0 = f*C2*Veq/V1

# =========================================================================== #
#                                   Calculs                                   #
# =========================================================================== #

N = 100000                          # nombre de régressions à effectuer

C0list = []                         # initialisation liste vide
for i in range(N):
    C2_simu = C2 + uC2*np.sqrt(3)*np.random.uniform(-1, 1)
    Veq_simu = Veq + uVeq*np.sqrt(3)*np.random.uniform(-1, 1)
    V1_simu = V1 + uV1*np.sqrt(3)*np.random.uniform(-1, 1)
    f_simu = f + uf*np.sqrt(3)*np.random.uniform(-1, 1)

    C0_simu = f_simu*C2_simu*Veq_simu/V1_simu

    C0list.append(C0_simu)

# =========================================================================== #
#                                 Utilisation                                 #
# =========================================================================== #

C0mean = np.mean(C0list)
uC0 = np.std(C0list, ddof=1)

print(f'C0 = {C0mean:.2f} ± {uC0:.2f}')
