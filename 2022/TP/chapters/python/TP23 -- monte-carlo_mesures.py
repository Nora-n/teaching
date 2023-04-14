# Disponible sur Capytale avec le code 4186-1558000

import numpy as np

# =========================================================================== #
#                              Incertitudes                                   #
# =========================================================================== #

f =  # dilution par 100
uf =  # uf/f = 1%
C2 =  # mol.L^-1
uC2 =  # uC2/C2 = 1%
V1 =  # L
uV1 =  # L
Veq =  # L
uVeq =  # L

C0 =

# =========================================================================== #
#                                   Calculs                                   #
# =========================================================================== #

N = 100000                          # nombre de régressions à effectuer

C0list = []                         # initialisation liste vide
for i in range(N):
    C2_simu = C2 +
    Veq_simu = Veq +
    V1_simu = V1 +
    f_simu = f +

    C0_simu = f_simu*C2_simu*Veq_simu/V1_simu

    C0list.append()

# =========================================================================== #
#                                 Utilisation                                 #
# =========================================================================== #

C0mean = np.mean(C0list)
uC0 = np.std(C0list, ddof=1)

print(f'C0 = {C0mean:.2f} ± {uC0:.2f}')
