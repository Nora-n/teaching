import numpy as np

d = 12               # cm
Delta_d = 0.1        # cm
D_d = [11.9, 12.1]   # cm
ud = 0.1/np.sqrt(3)  # cm
D = 50               # cm
Delta_D = 0.5        # cm
D_D = [49.5, 50.5]   # cm
uD = 0.5/np.sqrt(3)  # cm
f = D/4 - d**2/(4*D) # cm

uf_comp = 0.25*np.sqrt(
    uD**2 + (d**2/D)**2*(
        2*(ud/d)**2 + (uD/D)**2
    )
)

uf_comp_2 = 0.25*np.sqrt(
    uD**2*(1+d**4/D**4) +
    2*(d**2/D**2)*ud**2
)

print(f'f = {f:.2f} ± {uf_comp:.2f}')
print(f'f = {f:.2f} ± {uf_comp_2:.2f}')

N = 100000
liste_f = []
for i in range(0, N):
    d_simu = np.random.uniform(D_d[0], D_d[1])
    D_simu = np.random.uniform(D_D[0], D_D[1])
    f_simu = D_simu/4 - d_simu**2/(4*D_simu)
    liste_f.append(f_simu)

fmoy = np.mean(liste_f)
uf = np.std(liste_f, ddof=1)
print(f'f = {fmoy:.2f} ± {uf:.2f}')
