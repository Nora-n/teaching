import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'
plt.rc('text.latex',
       preamble=r'\usepackage[detect-all,locale=FR]{siunitx}[=v2]\usepackage{physics}')

fig = plt.figure(figsize=(7,5))
rect = 0.1, 0.10, 0.8, 0.8
ax = fig.add_axes(rect)
ax.grid()

def f(z,e):
    return z*(e+z)**2

e = 3
zlin = np.linspace(-e, 0, 1000)

ax.plot(zlin, f(zlin,e), color="cornflowerblue")
ax.margins(0, 0)
ax.set_xlabel('$z$')
ax.set_ylabel('$f(z)$')

ax.set_title(f'Représentation de $f(z)$ avec $e = {e}$')
fig.savefig("2023/07_DS/DS06/P1/figures/fz.pdf", bbox_inches="tight")

k = 1

def Ep(z, e, k, U):
    return 0.5*k*z**2 - U**2/2*(1/(e+z) - 1/e)
def dEp(z, e, k, U):
    return k*z + U**2/(2*(e+z)**2)

Um = np.sqrt((8*k*e**3)/(27))
print(Um**2/(2*k))

fig = plt.figure(figsize=(7,5))
rect = 0.1, 0.10, 0.8, 0.8
ax = fig.add_axes(rect)
ax.grid()

U = .33*Um

zlin = np.linspace(-e*0.99, 0.1, 1000)
ax.plot(zlin, Ep(zlin, e, k, U),
        color="cornflowerblue",
        label="$\\mathcal{E}_p$")
zlin = np.linspace(-e*0.90, 0.1, 1000)
ax.plot(zlin, dEp(zlin, e, k, U),
        color="orange",
        label="$\\dv{\\mathcal{E}_p}{z}$")

ax.margins(0, 0)
ax.set_xlabel('$z$')
ax.set_ylabel('$\\mathcal{E}_p(z)$')

ax.legend()

ax.set_title(f'Représentation de $\\mathcal{{E}}_p(z)$ avec $e = {e}$')
fig.savefig("2023/07_DS/DS06/P1/figures/Epz.pdf", bbox_inches="tight")
