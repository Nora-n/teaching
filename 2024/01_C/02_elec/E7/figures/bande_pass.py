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
Q = 3
wr = w0 * np.sqrt(Q**2 - 0.5) / (Q)

wlist = np.linspace(w0 / 2, 3 * w0 / 2, 1000)
xmin, xmax = [min(wlist), max(wlist)]


def I(w, Q=Q):
    x = w / w0
    return 1 / (1 + 1j * Q * (x - 1 / x))


fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

Qlist = [3, 7]
ucls = ["firebrick", "cornflowerblue"]

ampl_dict = {Q: np.abs(I(wlist, Q=Q)) for Q in Qlist}

ampl_max = max(ampl_dict[3])
ampl_eff = [ampl_max / np.sqrt(2) for w in wlist]

idx_cross = {
    Q: np.argwhere(np.diff(np.sign(ampl_dict[Q] - ampl_eff))).flatten() for Q in Qlist
}

w1 = {Q: wlist[idx_cross[Q][0]] for Q in Qlist}
w2 = {Q: wlist[idx_cross[Q][1]] for Q in Qlist}

ymin, ymax = [0, 1.1 * ampl_max]

ax.axvline(w0, ls="--", lw=1.5, color="black")

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
ax.xaxis.set_label_coords(0.90, -0.02)
ax.set_ylabel("$X(\\omega)$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([w1[7], w0, w2[7]])
ax.set_xticklabels(["$\\omega_1$", "$\\omega_r$", "$\\omega_2$"])
ax.set_yticks([ampl_eff[0], ampl_max])
ax.set_yticklabels(
    ["$\\displaystyle\\frac{X_{\\mathrm{max}}}{\\sqrt{2}}$", "$X_{\\mathrm{max}}$"]
)

# ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

fig.savefig("./bande_pass_stud.pdf", bbox_inches="tight")

for Q, cl in zip(Qlist, ucls):
    ax.plot(wlist, ampl_dict[Q], color=cl)
    # , label=f"$Q = {Q}$")

ax.fill_between(
    [w1[7], w2[7]],
    0.98 * ampl_eff[0],
    1.02 * ampl_eff[0],
    color="cornflowerblue",
    alpha=0.3,
    label="$\\Delta\\omega$",
    zorder=7,
)

# ax.plot(wrspace, Uspace, ls=":", lw=1, color="black", label="$U_{\\mathrm{max}}(Q)$")

ax.legend(fontsize=15)

fig.savefig("./bande_pass_prof.pdf", bbox_inches="tight")
