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

E0 = 10  # V
R = 1e3  # O
L = 9.9e-2  # H
C = 0.10e-6  # F
w0 = 10_000  # rad.s^-1
Q = 1.5
wr = w0 * np.sqrt(Q**2 - 0.5) / (Q)

wlist = np.linspace(1e-3, 5 * w0, 1000)
xlist = wlist / w0
xmin, xmax = [min(xlist), max(xlist)]


def Uc(x, Q=Q):
    return 1 / (1 + 1j * Q * (x - 1 / x))


fig = plt.figure(figsize=(10, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

Qlist = [0.1, 0.7, 1, 3]
ucls = ["firebrick", "limegreen", "cornflowerblue", "violet"]

ampl_dict = {Q: np.abs(Uc(xlist, Q=Q)) for Q in Qlist}

ymin, ymax = [0, 1.1]

ax.axvline(1, ls="--", lw=1.5, color="black")
ax.axhline(1, ls="--", lw=1.5, color="black")

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel("$x = \\omega/\\omega_0$", fontsize=15, clip_on=False)
ax.xaxis.set_label_coords(0.90, -0.02)
ax.set_ylabel("$U/(RI_0)$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([1])
ax.set_xticklabels([1])
ax.set_yticks([0, 1])

# ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

# ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

for Q, cl in zip(Qlist, ucls):
    ax.plot(xlist, ampl_dict[Q], color=cl, label=f"$Q = {Q}$")

ax.legend(fontsize=15)

fig.savefig("./rlc_parr_U_ampl.pdf", bbox_inches="tight")
