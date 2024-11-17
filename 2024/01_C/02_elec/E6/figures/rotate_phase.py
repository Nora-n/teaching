import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

import numpy as np
import pandas as pd

from IPython.display import Latex, display

plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "EB Garamond",
        "axes.labelsize": "x-large",
        "xtick.labelsize": "x-large",
        "ytick.labelsize": "x-large",
    }
)
plt.rcParams["figure.facecolor"] = "w"
plt.rcParams["animation.html"] = "jshtml"

mpl.rc("text.latex", preamble=r"\usepackage{xcolor}\usepackage{amsmath}")

fig, ax = plt.subplots()
# t = np.linspace(0, 3, 40)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t
#
# v02 = 5
# z2 = g * t**2 / 2 + v02 * t
#
# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f"v0 = {v0} m/s")
# line2 = ax.plot(t[0], z2[0], label=f"v0 = {v02} m/s")[0]
# ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel="Time [s]", ylabel="Z [m]")
# ax.legend()

E0 = 5  # V
R = 100  # O
C = 0.1e-6  # F
f = 10000  # Hz
w = 2 * np.pi * f  # rad.s^-1

an = np.linspace(0, 2 * np.pi, 360)
ax.plot(E0 * np.cos(an), E0 * np.sin(an), label="$E_0$")
arr = ax.arrow(
    x=0,
    y=0,
    dx=E0 * np.cos(an[0]),
    dy=E0 * np.sin(an[0]),
    width=0.01,
    length_includes_head=True,
    head_width=0.1,
    head_length=0.1,
    fc="black",
    label="$U_c = \\frac{E_0}{1+\\mathrm{j}RC\omega}$",
)
ax.set_aspect("equal")
leg = ax.legend(ncol=2, fontsize=20, loc="lower center", bbox_to_anchor=(0.5, 1))


def U(w):
    return E0 / (1 + 1j * R * C * w)


def update(frame):
    # update amplitude:
    Uc = np.abs(U(w))
    # update the arrow plot:
    arr.set_data(
        dx=Uc * np.cos(an[frame]),
        dy=Uc * np.sin(an[frame]),
    )
    # update legend:
    # leg.get_texts()[0].set_text(lab) #Update label each at frame
    return arr


print(f"Uc(w) = {np.abs(U(w))}")

# ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=30)
# FFwriter = animation.FFMpegWriter(fps=30)
# ani.save("first_test.mp4", writer=FFwriter, dpi=500)

fig.savefig("./first_test.pdf", bbox_inches="tight")
