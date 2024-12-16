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

################## TIMESERIES ##################

w = 7.5e3  # rad.s^-
T = 2 * np.pi / w  # s
f = 1 / T  # Hz
k = 19.8  # rad.s^-1
L = 2 * np.pi / k  # m
c = L * f  # m.s^-1
A = 1  # V

nT = 1
tlist = np.linspace(-nT * T, nT * T, 1000)
xmin, xmax = [min(tlist), max(tlist)]

xlist = [0, L / 4, L / 2]
ucls = ["firebrick", "limegreen", "cornflowerblue"]


def ufunc(t, x):
    return A * np.cos(w * t + k * x)


u = np.vectorize(ufunc, otypes=[np.float64])

fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)
    ax.spines[axe].set_position("zero")

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

u_dict = {x: u(tlist, x) for x in xlist}

# ymin, ymax = [min(u_list**2), max(u_list)]

for x, cl, lbl, lss in zip(
    xlist,
    ucls,
    ["0", "$\\frac{\\lambda}{4}$", "$\\frac{\\lambda}{2}$"],
    ["-", "--", ":"],
):
    ax.plot(
        tlist, u_dict[x], ls=lss, color=cl, lw=2, label="$s($" + lbl + "$,t)$", zorder=1
    )
# ax.axhline(0.5, ls="--", lw=2, color="black")
# ax.axvline(Vlim, c="k", ls="--", lw=1)

ax.legend(fontsize=15, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.05))

# ax.grid(visible=True, which="both")

ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t$ (s)", fontsize=15, clip_on=False, zorder=7)
ax.xaxis.set_label_coords(0.98, 0.60)
ax.set_ylabel("$s(x,t)$", fontsize=15, rotation=0, clip_on=False)
ax.yaxis.set_label_coords(0.5, 1.05)

tckslist = np.arange(-4, 4.1, 1)
ax.set_xticks(T / 4 * tckslist)
# plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
# lbls = ax.get_xticklabels()
ax.set_xticklabels(
    [
        "$-T$",
        "$\\displaystyle-\\frac{3T}{4}$",
        "$\\displaystyle-\\frac{T}{2}$",
        "$\\displaystyle-\\frac{T}{4}$",
        "$0$",
        "$\\displaystyle\\frac{T}{4}$",
        "$\\displaystyle\\frac{T}{2}$",
        "$\\displaystyle\\frac{3T}{4}$",
        "$T$",
    ]
    # [f"$\\displaystyle-\\frac{{T}}{{{int(abs(tck))}}}$" for tck in tckslist if tck <= 0]
    # + [f"$\\displaystyle\\frac{{T}}{{{int(abs(tck))}}}$" for tck in tckslist if tck > 0]
)
ax.set_yticks([])
# ax.set_yticklabels(["$P_{\\mathrm{max}} = K^\\circ P^\\circ$"])
# ax.set_yticklabels(["$P_{\\mathrm{max}}$"])

for label in ax.get_xticklabels():
    label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.7))

ax.tick_params(which="major", length=7, width=2)

# ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="x")

ax.plot(0.5, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0.5, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

# plt.show()

fig.savefig("./prop_l2l4.pdf", bbox_inches="tight")
