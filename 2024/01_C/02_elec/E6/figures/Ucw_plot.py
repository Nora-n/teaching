import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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

mpl.rc("text.latex", preamble=r"\usepackage{xcolor}\usepackage{amsmath}")

################### AMPLITUDE ###################

E0 = 5  # V
R = 10e3  # O
C = 0.1e-6  # F
f = 10e3  # Hz
w = 2 * np.pi * f  # rad.s^-1
wc = 1 / (R * C)


wlist = np.linspace(0, 10 * wc, 1000)
xmin, xmax = [min(wlist), max(wlist)]


def Uc(w, E0=E0, R=R, C=C):
    return E0 / (1 + 1j * R * C * w)


fig = plt.figure(figsize=(5, 5), constrained_layout=True)
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ampl_list = np.abs(Uc(wlist))
ymin, ymax = [min(ampl_list), max(ampl_list)]

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
# ax.xaxis.set_label_coords(1.05, 0.02)
ax.set_ylabel("$U_C(\\omega)~[\\mathrm{V}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.get_xaxis_transform(), clip_on=False)
ax.plot(1, 0.5, ">k", lw=2, ms=5, transform=ax.get_yaxis_transform(), clip_on=False)

fig.savefig("./Ucw_ampl_stud.pdf", bbox_inches="tight")

ax.plot(wlist, ampl_list, color="firebrick")

fig.savefig("./Ucw_ampl_prof.pdf", bbox_inches="tight")

################### ARGUMENT ###################

# wlist = np.linspace(0, 5 * wc, 1000)
# xmin, xmax = [min(wlist), max(wlist)]

fig = plt.figure(figsize=(5, 5), constrained_layout=True)
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "top"]:
    # ax.spines[axe].set_position("center")
    ax.spines[axe].set_linewidth(2)

for axe in ["bottom", "right"]:
    ax.spines[axe].set_visible(False)

arg_list = np.angle(Uc(wlist))
ymin, ymax = [min(arg_list), max(arg_list)]

ax.axhline(-np.pi / 2, ls="--", color="black")

ax.set_xlim(xmin, xmax)
ax.set_ylim(-1.60, ymax + 0.07)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
ax.xaxis.set_label_coords(0.90, 0.98)
ax.set_ylabel("$\\varphi(\\omega)~[\\mathrm{rad}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks(np.arange(2000, 10001, 2000))
ax.set_yticks([*np.arange(0, -1.6, -0.2), -np.pi / 2])
ax.set_yticklabels(
    [0, -0.2, -0.4, -0.6, -0.8, -1.0, -1.2, -1.4, "-$\\displaystyle\\frac{\\pi}{2}$"],
)

ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 1, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

fig.savefig("./Ucw_arg_stud.pdf", bbox_inches="tight")

ax.plot(wlist, arg_list, color="firebrick")

fig.savefig("./Ucw_arg_prof.pdf", bbox_inches="tight")
