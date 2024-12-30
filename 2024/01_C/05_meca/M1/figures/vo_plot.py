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
v0 = 3  # m.s^-1

tlist = np.linspace(0, 3, 100)
xmin, xmax = [min(tlist), max(tlist)]


def vy(t):
    return -g * t


def vx(t):
    return v0


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
ax.xaxis.set_label_coords(0.95, 0.93)
ax.set_ylabel("$v(t)~[\\mathrm{m}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([])
# ax.set_xticklabels(["$\\omega_r$", "$\\omega_0$"])
ax.set_yticks([])

ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0.87, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

ax.plot(tlist, [v0 for k in range(len(tlist))], lw=2, ls="none", label="$v_x(t)$")
ax.plot(tlist, vy(tlist), lw=2, ls="None", label="$v_y(t)$")

ax.legend(fontsize=15)

fig.savefig("./vo_vv_stud.pdf", bbox_inches="tight")

# not empty for prof
for line in ax.lines:
    line.set_label(s="")

ax.plot(
    tlist,
    [v0 for k in range(len(tlist))],
    lw=2,
    ls="--",
    color="black",
    label="$v_x(t)$",
)
ax.plot(tlist, vy(tlist), lw=2, color="black", label="$v_y(t)$")

ax.legend(fontsize=15)

fig.savefig("./vo_vv_prof.pdf", bbox_inches="tight")

################### Position ###################


def y(t):
    return -0.5 * g * t**2


def x(t):
    return v0 * t


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
ax.xaxis.set_label_coords(0.95, 0.88)
ax.set_ylabel("OM$(t)~[\\mathrm{m}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([])
# ax.set_xticklabels(["$\\omega_r$", "$\\omega_0$"])
ax.set_yticks([])

ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0.80, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

ax.plot(tlist, x(tlist), lw=2, ls="None", label="$x(t)$")
ax.plot(tlist, y(tlist), lw=2, ls="None", label="$y(t)$")

ax.legend(fontsize=15)

fig.savefig("./vo_xx_stud.pdf", bbox_inches="tight")

# not empty for prof
for line in ax.lines:
    line.set_label(s="")

ax.plot(tlist, x(tlist), lw=2, ls="--", color="black", label="$x(t)$")
ax.plot(tlist, y(tlist), lw=2, color="black", label="$y(t)$")

ax.legend(fontsize=15)

fig.savefig("./vo_xx_prof.pdf", bbox_inches="tight")
