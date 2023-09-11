import numpy as np

d = 12               # cm
Delta_d = 0.1        # cm
ud = 0.1/np.sqrt(3)  # cm
D = 50               # cm
Delta_D = 0.5        # cm
uD = 0.5/np.sqrt(3)  # cm
f = D/4 - d**2/(4*D) # cm

uf_comp = 0.25*np.sqrt(
    uD**2 + (d**2/D)**2*(
        2*(ud/d)**2 + (uD/D)**2
    )
)

print(f'f = {f:.2f} ± {uf_comp:.2f}')

N = 10000
flist = []
for i in range(0, N):
    d_simu = d + Delta_d*np.random.uniform(-1, 1)
    D_simu = D + Delta_D*np.random.uniform(-1, 1)
    f_simu = D_simu/4 - d_simu**2/(4*D_simu)
    flist.append(f_simu)

uf_mc = np.std(flist, ddof=1)
print(f'f = {f:.2f} ± {uf_mc:.2f}')
