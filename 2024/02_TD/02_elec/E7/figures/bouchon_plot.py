import numpy as np
import matplotlib as mpl
import matplotlib.ticker as tck
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

## TENSION

################### AMPLITUDE ###################

E0 = 5  # V
R = 1e3  # O
L = 1e-3  # H
C = 5.6e-8  # F
f0 = 22.5e3  # Hz
w0 = 2 * np.pi * f0  # rad.s^-1
Q = 7.5
# wr = w0 * np.sqrt(Q**2 - 0.5) / (Q)

flist = np.linspace(1e-3, 40, 5000) * 1e3
wlist = 2 * np.pi * flist
xmin, xmax = [0, max(flist)]


def Uc(f, Q=Q):
    x = f / f0
    return E0 / (1 + 1j * Q * (x - 1 / x))


fig = plt.figure(figsize=(7.5, 2.5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

# for axe in ["left", "bottom"]:
#     ax.spines[axe].set_linewidth(2)
#
# for axe in ["top", "right"]:
#     ax.spines[axe].set_visible(False)

ampl_list = np.abs(Uc(wlist, Q=Q))

ymin, ymax = [min(ampl_list), max(ampl_list)]

ax.axvline(w0, ls="--", lw=1.5, color="black")

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, 6)

ax.set_xlabel("$f~[\\mathrm{kHz}]$", fontsize=15, clip_on=False)
# ax.xaxis.set_label_coords(0.90, -0.02)
ax.set_ylabel("$U~~[\\mathrm{V}]$", fontsize=15)  # , rotation=0)
# ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks(np.arange(0, 41, 5) * 1e3)
ax.set_xticklabels(np.arange(0, 41, 5))
ax.set_xticks(np.arange(0, 41, 1) * 1e3, minor=True)
ax.set_xticklabels(["" for k in range(len(np.arange(0, 41, 1)))], minor=True)
ax.set_yticks(np.arange(0, 6, 1))
ax.set_yticks(np.arange(0, 6.1, 0.25), minor=True)

# ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid(lw=1.5)
ax.grid(which="minor", ls="--", lw=1)

# ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
# ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

# fig.savefig("./rlc_Uc_ampl_stud.pdf", bbox_inches="tight")

ax.plot(wlist, ampl_list, color="firebrick")

fig.savefig("./bouchon_plot.pdf", bbox_inches="tight")
