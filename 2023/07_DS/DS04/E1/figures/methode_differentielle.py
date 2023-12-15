import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'
plt.rc('text.latex',
       preamble=r'\usepackage[detect-all,locale=FR]{siunitx}[=v2]')

fig = plt.figure(figsize=(7,5))
rect = 0.1, 0.10, 0.8, 0.8
ax = fig.add_axes(rect)

O2 = np.array([0.25,1.07,1.78,3.02])*1e-4
v0 = np.array([0.29,1.11,2.27,3.32])*1e-6
y = np.log(v0)
x = np.log(O2)

a, b = np.polyfit(x,y,1)

ax.scatter(x, y, s=200,
           marker="+", color="orange", label="Données")
ax.plot(x, a*x+b,
        color="cornflowerblue", label="Régression")
ax.set_xlabel("$x$",fontsize=20)
ax.set_ylabel("$y$",fontsize=20)
ax.legend(fontsize=15)
ax.set_title(fr"$y=\num{{{b:.2f}}}+\num{{{a:.1f}}}x$",
             fontsize=25)
fig.savefig("2023/07_DS/DS04/E1/figures/trace_lnv.pdf", bbox_inches="tight")
