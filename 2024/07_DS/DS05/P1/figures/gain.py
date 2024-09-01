# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:52:44 2021

@author: samba
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 20,
    "xtick.labelsize": 20,
    "ytick.labelsize": 20})
plt.rcParams['figure.facecolor'] = 'w'

xmax=6
x = np.linspace(0,xmax,200)
Q = 1
G = 1/np.sqrt((1-x**2)**2+x**2/Q**2)
xR= np.sqrt(1-1/(2*Q**2))
Gmax=1/np.sqrt((1-xR**2)**2+xR**2/Q**2)
print(Gmax)

plt.plot(x,G)
ax = plt.gca()
plt.xlim(0,6)
plt.ylim(0,1.1*Gmax)
plt.text(xR, -0.08, r'$x_r$', ha="center", fontsize=20)
plt.axvline(xR,0,1/1.1,color='gray',linestyle='--')
plt.axhline(Gmax,0,xR/xmax,color='gray',linestyle='--')
# plt.title("Gain en fonction de la pulsation réduite")
plt.xlabel("Pulsation réduite $x$", fontsize=20)
plt.ylabel("$G/H_0$", fontsize=20)
# plt.show()
plt.savefig("./2023/07_DS/DS05/P1/figures/gain.pdf", bbox_inches="tight")
