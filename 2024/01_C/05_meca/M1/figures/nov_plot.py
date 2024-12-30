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

################### Vitesse ###################

g = 9.81  # m.s^-2

tlist = np.linspace(0, 3, 100)
xmin, xmax = [min(tlist), max(tlist)]


def vy(t):
    return -g * t


fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

ax.spines["bottom"].set_position("zero")

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t~[\\mathrm{s}]$", fontsize=15, clip_on=False)
ax.xaxis.set_label_coords(0.95, 1.05)
ax.set_ylabel("$v_y(t)~[\\mathrm{m}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([])
# ax.set_xticklabels(["$\\omega_r$", "$\\omega_0$"])
ax.set_yticks([])

ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0.955, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

ax.plot(tlist, vy(tlist), lw=2, ls="None")

fig.savefig("./nov_vy_stud.pdf", bbox_inches="tight")

ax.plot(tlist, vy(tlist), lw=2, color="black")

# ax.legend(fontsize=15)

fig.savefig("./nov_vy_prof.pdf", bbox_inches="tight")

################### Position ###################


def y(t):
    return -0.5 * g * t**2


fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

ax.spines["bottom"].set_position("zero")

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t~[\\mathrm{s}]$", fontsize=15, clip_on=False)
ax.xaxis.set_label_coords(0.95, 1.05)
ax.set_ylabel("$y(t)~[\\mathrm{m}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([])
# ax.set_xticklabels(["$\\omega_r$", "$\\omega_0$"])
ax.set_yticks([])

ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0.955, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

ax.plot(tlist, y(tlist), lw=2, ls="None")

fig.savefig("./nov_y_stud.pdf", bbox_inches="tight")

ax.plot(tlist, y(tlist), lw=2, color="black")

# ax.legend(fontsize=15)

fig.savefig("./nov_y_prof.pdf", bbox_inches="tight")
