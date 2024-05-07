import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'

zam = 1
w0 = 1
tau = 1

def Z_flo(x):
    return zam/(np.sqrt((1/x**2-1)**2 + 1/(x*w0*tau)**2))

def Z_nor(x):
    return (x**2)*zam/(np.sqrt((1-x**2)**2 + (x/(w0*tau))**2))

xlin = np.linspace(0, 10, 1000)

xr_nor = np.sqrt(2*(w0*tau)**2-1)/(w0*tau*np.sqrt(2))
xr_flo = 1/xr_nor

Zmax = np.max(Z_nor(xlin))

fig = plt.figure(figsize=(10,8))
ax = fig.add_axes((0.1, 0.12, 0.90, 0.80))

ax.plot(xlin,Z_flo(xlin),
        color='cornflowerblue',
        label='Florence')
ax.plot(xlin,Z_nor(xlin),
        color='orange',
        label='Nora')

ax.plot([xr_flo, xr_flo], [0, Zmax])
ax.plot([xr_nor, xr_nor], [0, Zmax])

ax.legend()

plt.show()
