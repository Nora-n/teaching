import numpy as np
import matplotlib as mpl
import matplotlib.ticker as tck
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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

mpl.rc(
    "text.latex",
    preamble=r"\usepackage{xcolor}\usepackage{amsmath}\usepackage[detect-all,locale=FR,separate-uncertainty]{siunitx}[=v2]",
)

################### Vitesse ###################

m = 60  # kg
g = 9.81  # m.s^-2
B = 0.25  # kg.m^-1
vlim = np.sqrt(m * g / B)  # m.s^-1
T = np.sqrt(m / (B * g))  # s
print(f"vlim = {vlim:.1f} m.s^-1 = {vlim*3.6:.1f} km.h^-1")
print(f"T = {T:.2f} s")

t = np.arange(0, 4 * T, 0.1 * T)  # s
xmin, xmax = [min(t), max(t)]


def vquad(y, t):
    return g - B / m * y**2


y0 = 0
sol = odeint(vquad, y0, t)

fig = plt.figure(figsize=(8, 3))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

ax.spines["bottom"].set_position("zero")

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ax.set_xlim(xmin, xmax)
ax.set_ylim(0, 50)

ax.set_xlabel("$t~[\\mathrm{s}]$", fontsize=15, clip_on=False)
ax.xaxis.set_label_coords(0.97, -0.02)
ax.set_ylabel("$v(t)~[\\mathrm{m}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([])
# ax.set_xticklabels(["$\\omega_r$", "$\\omega_0$"])
ax.set_yticks([])

ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

ax.plot(t, sol, lw=2, c="none")
ax.plot([T, T, 0], [0, sol[10][0], sol[10][0]], ls="none", c="k")

ax.text(
    T,
    -1.00,
    "$T$",
    ha="center",
    va="top",
    fontsize=15,
    color="white",
    # transform=ax.transAxes,
)
ax.text(
    -0.20,
    0.76 * vlim,
    "$\\num{0.76}\\,v_{\\mathrm{lim}}$",
    ha="right",
    va="center",
    fontsize=15,
    color="white",
    # transform=ax.transAxes,
)

fig.savefig("./cl_fq_v_stud.pdf", bbox_inches="tight")

ax.plot(t, sol, lw=2, c="firebrick")
ax.axhline(vlim, ls="--", c="k")
ax.plot([T, T, 0], [0, sol[10][0], sol[10][0]], ls="--", c="k")

ax.text(
    T,
    -1.00,
    "$T$",
    ha="center",
    va="top",
    fontsize=15,
    # transform=ax.transAxes,
)
ax.text(
    -0.20,
    0.76 * vlim,
    "$\\num{0.76}\\,v_{\\mathrm{lim}}$",
    ha="right",
    va="center",
    fontsize=15,
    # transform=ax.transAxes,
)
ax.text(
    -0.20,
    vlim,
    "$v_{\\mathrm{lim}}$",
    ha="right",
    va="center",
    fontsize=15,
    # transform=ax.transAxes,
)
# ax.legend(fontsize=15)

fig.savefig("./cl_fq_v_prof.pdf", bbox_inches="tight")
