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

################### TAN ###################

fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for mut in [-3, -1, 1, 3]:
    ax.axvline(mut * np.pi / 2, ls="--", color="k", lw=1, zorder=1)

ax.set_xlim(-3 * np.pi / 2, 3 * np.pi / 2)
ax.set_ylim(-10, 10)

ax.set_xlabel("$\\theta$", fontsize=15)
ax.xaxis.set_label_coords(1.05, 0.52)
ax.set_ylabel("$\\tan(\\theta)$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0.5, 1.02)

ax.set_yticks([])
ax.set_xticks([-3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2])
ax.set_xticklabels(
    [
        "$-\\frac{3\\pi}{2}$",
        "$-\\pi$",
        "$-\\frac{\\pi}{2}$",
        "$\\frac{\\pi}{2}$",
        "$\\pi$",
        "$\\frac{3\\pi}{2}$",
    ],
)

for axe in ["left", "bottom"]:
    ax.spines[axe].set_position("center")
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.get_xaxis_transform(), clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.get_yaxis_transform(), clip_on=False)

for tick in [0, 2, 3, 5]:
    ax.get_xticklabels()[tick].set_backgroundcolor("white")
    ax.get_xticklabels()[tick].set_zorder(3)

ext = 1.05
inn = 0.98

th = [
    np.linspace(-np.pi, -ext * np.pi / 2, 200),
    np.linspace(-inn * np.pi / 2, inn * np.pi / 2, 100),
    np.linspace(ext * np.pi / 2, np.pi, 200),
]

clrs = ["firebrick", "cornflowerblue", "limegreen"]
lbls = [
    "$\\displaystyle\\theta \\in \\bigg] -\\frac{3\\pi}{2}, - \\frac{\\pi}{2} \\bigg[$",
    "$\\displaystyle\\theta \\in \\bigg] -\\frac{\\pi}{2}, \\frac{\\pi}{2} \\bigg[$",
    "$\\displaystyle\\theta \\in \\bigg] \\frac{\\pi}{2}, \\frac{3\\pi}{2} \\bigg[$",
    # "$\\displaystyle\\bigg] -\\frac{3\\pi}{2}, - \\frac{\\pi}{2} \\bigg[$",
    # "$\\displaystyle\\bigg] -\\frac{\\pi}{2}, \\frac{\\pi}{2} \\bigg[$",
    # "$\\displaystyle\\bigg] \\frac{\\pi}{2}, \\frac{3\\pi}{2} \\bigg[$",
]

for k, tt, cc, ll in zip(range(len(th)), th, clrs, lbls):
    ax.plot(tt, np.tan(tt), color=cc, label=ll, lw=2, zorder=4)
    # ax.scatter()

th_alph = [
    np.linspace(-inn * 3 * np.pi / 2, -np.pi, 200),
    np.linspace(np.pi, inn * 3 * np.pi / 2, 200),
]

for k, tt, cc in zip(range(len(th_alph)), th_alph, ["firebrick", "limegreen"]):
    ax.plot(tt, np.tan(tt), color=cc, lw=2, alpha=0.5, zorder=4)

tplt_inf0 = [-np.pi / 3, 2 * np.pi / 3]
crls_inf0 = ["cornflowerblue", "limegreen"]
txt_inf0 = ["$-\\frac{\\pi}{3}$", "$\\frac{2\\pi}{3}$"]

tplt_sup0 = [-2 * np.pi / 3, np.pi / 3]
crls_sup0 = ["firebrick", "cornflowerblue"]
txt_sup0 = ["$-\\frac{2\\pi}{3}$", "$-\\frac{\\pi}{3}$"]

for x, y, cc, txt in zip(tplt_inf0, np.tan(tplt_inf0), crls_inf0, txt_inf0):
    ax.scatter(x, y, s=100, c=cc, zorder=4)
    ax.text(x + 0.2, y, s=txt, ha="left", va="top", fontsize=15)

for x, y, cc, txt in zip(tplt_sup0, np.tan(tplt_sup0), crls_sup0, txt_sup0):
    ax.scatter(x, y, s=100, c=cc, zorder=4)
    ax.text(x - 0.2, y, s=txt, ha="right", va="bottom", fontsize=15)

ax.legend(
    fontsize=10,
    ncol=3,
    columnspacing=2,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.15),
)

fig.savefig("./fig_tan.pdf", bbox_inches="tight")

################### ARCTAN ###################

fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

tan = np.linspace(-10, 10, 300)

for k, cc, ll, lss in zip(range(len(clrs)), clrs, lbls, ["--", "-", "--"]):
    ax.plot(
        tan,
        np.atan(tan) + (k - 1) * (np.pi),
        color=cc,
        label=ll,
        lw=2,
        ls=lss,
        zorder=4,
    )

tplt_inf0 = [-np.pi / 3, 2 * np.pi / 3]
crls_inf0 = ["cornflowerblue", "limegreen"]
txt_inf0 = ["$-\\frac{\\pi}{3}$", "$\\frac{2\\pi}{3}$"]

tplt_sup0 = [-2 * np.pi / 3, np.pi / 3]
crls_sup0 = ["firebrick", "cornflowerblue"]
txt_sup0 = ["$-\\frac{2\\pi}{3}$", "$-\\frac{\\pi}{3}$"]

for x, y, cc, txt in zip(np.tan(tplt_inf0), tplt_inf0, crls_inf0, txt_inf0):
    ax.scatter(x, y, s=100, c=cc, zorder=4)
    ax.text(x - 0.3, y, s=txt, ha="right", va="bottom", fontsize=15)

for x, y, cc, txt in zip(np.tan(tplt_sup0), tplt_sup0, crls_sup0, txt_sup0):
    ax.scatter(x, y, s=100, c=cc, zorder=4)
    ax.text(x + 0.2, y, s=txt, ha="left", va="top", fontsize=15)

ax.arrow(
    np.tan(tplt_inf0[0]),
    tplt_inf0[0],
    0,
    np.pi - 0.2,
    ec="limegreen",
    fc="limegreen",
    width=0.01,
    length_includes_head=True,
    head_width=0.4,
    head_length=0.2,
    zorder=5,
)
ax.text(
    np.tan(tplt_inf0[0]) - 0.5,
    tplt_inf0[0] + np.pi / 2,
    "$+\\pi$",
    ha="right",
    va="center",
    fontsize=18,
    color="limegreen",
    bbox=dict(facecolor="none", ec="limegreen", lw=3, alpha=0.5),
    zorder=5,
)

ax.arrow(
    np.tan(tplt_sup0[1]),
    tplt_sup0[1],
    0,
    -np.pi + 0.2,
    ec="firebrick",
    fc="firebrick",
    width=0.01,
    length_includes_head=True,
    head_width=0.4,
    head_length=0.2,
    zorder=5,
)
ax.text(
    np.tan(tplt_sup0[1]) + 0.5,
    tplt_sup0[1] - np.pi / 2,
    "$-\\pi$",
    ha="left",
    va="center",
    fontsize=18,
    color="firebrick",
    bbox=dict(facecolor="none", ec="firebrick", lw=3, alpha=0.5),
    zorder=5,
)

for mut in [-3, -1, 1, 3]:
    ax.axhline(mut * np.pi / 2, ls="--", color="k", lw=1, zorder=1)

ax.set_xlim(-10, 10)
ax.set_ylim(-3 * np.pi / 2, 3 * np.pi / 2)

ax.set_xlabel("$x$", fontsize=15)
ax.xaxis.set_label_coords(1.05, 0.52)
ax.set_ylabel("$\\arctan(x)$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0.5, 1.02)

ax.set_xticks([])
ax.set_yticks([-3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2])
ax.set_yticklabels(
    [
        "$-\\frac{3\\pi}{2}$",
        "$-\\pi$",
        "$-\\frac{\\pi}{2}$",
        "$\\frac{\\pi}{2}$",
        "$\\pi$",
        "$\\frac{3\\pi}{2}$",
    ],
)

for axe in ["left", "bottom"]:
    ax.spines[axe].set_position("center")
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.get_xaxis_transform(), clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.get_yaxis_transform(), clip_on=False)

for tick in [0, 2, 3, 5]:
    ax.get_yticklabels()[tick].set_backgroundcolor("white")
    ax.get_yticklabels()[tick].set_zorder(3)

ax.legend(
    fontsize=10,
    ncol=3,
    columnspacing=2,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.15),
)

fig.savefig("./fig_atan.pdf", bbox_inches="tight")

################### ARCTANTAN ###################

fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

ext = 1.05
inn = 0.98

th = [
    np.linspace(-inn * 3 * np.pi / 2, -ext * np.pi / 2, 200),
    np.linspace(-inn * np.pi / 2, inn * np.pi / 2, 100),
    np.linspace(ext * np.pi / 2, inn * 3 * np.pi / 2, 200),
]

clrs = ["firebrick", "cornflowerblue", "limegreen"]
lbls = [
    "$\\displaystyle\\theta \\in \\bigg] -\\frac{3\\pi}{2}, - \\frac{\\pi}{2} \\bigg[$",
    "$\\displaystyle\\theta \\in \\bigg] -\\frac{\\pi}{2}, \\frac{\\pi}{2} \\bigg[$",
    "$\\displaystyle\\theta \\in \\bigg] \\frac{\\pi}{2}, \\frac{3\\pi}{2} \\bigg[$",
    # "$\\displaystyle\\bigg] -\\frac{3\\pi}{2}, - \\frac{\\pi}{2} \\bigg[$",
    # "$\\displaystyle\\bigg] -\\frac{\\pi}{2}, \\frac{\\pi}{2} \\bigg[$",
    # "$\\displaystyle\\bigg] \\frac{\\pi}{2}, \\frac{3\\pi}{2} \\bigg[$",
]

for k, tt, cc, ll, lss in zip(range(len(th)), th, clrs, lbls, ["--", "-", "--"]):
    ax.plot(tt, np.atan(np.tan(tt)), color=cc, label=ll, lw=2, ls=lss, zorder=4)
    # ax.scatter()

tplt_inf0 = [-np.pi / 3, 2 * np.pi / 3]
crls_inf0 = ["cornflowerblue", "limegreen"]
txt_inf0 = ["$-\\frac{\\pi}{3}$", "$\\frac{2\\pi}{3}$"]

tplt_sup0 = [-2 * np.pi / 3, np.pi / 3]
crls_sup0 = ["firebrick", "cornflowerblue"]
txt_sup0 = ["$-\\frac{2\\pi}{3}$", "$-\\frac{\\pi}{3}$"]

for x, y, cc, txt in zip(tplt_inf0, np.atan(np.tan(tplt_inf0)), crls_inf0, txt_inf0):
    ax.scatter(x, y, s=100, c=cc, zorder=4)
    ax.text(x, y - 0.3, s=txt, ha="center", va="top", fontsize=15)

for x, y, cc, txt in zip(tplt_sup0, np.atan(np.tan(tplt_sup0)), crls_sup0, txt_sup0):
    ax.scatter(x, y, s=100, c=cc, zorder=4)
    ax.text(x - 0.2, y + 0.3, s=txt, ha="center", va="bottom", fontsize=15)

ax.arrow(
    tplt_inf0[0],
    tplt_inf0[0],
    np.pi - 0.2,
    0,
    ec="limegreen",
    fc="limegreen",
    width=0.01,
    length_includes_head=True,
    head_width=0.2,
    head_length=0.2,
    zorder=5,
)
ax.text(
    tplt_inf0[0] + np.pi / 2,
    tplt_inf0[0] - 0.3,
    "$+\\pi$",
    ha="center",
    va="top",
    fontsize=18,
    color="limegreen",
    bbox=dict(facecolor="none", ec="limegreen", lw=3, alpha=0.5),
    zorder=5,
)
ax.text(
    2 * np.pi / 3 + 0.27,
    tplt_inf0[0] - np.pi / 2,
    "$\\theta_{\\rm vrai} = \\arctan(\\tan(\\theta))+\\pi$",
    ha="center",
    va="top",
    fontsize=12,
    color="limegreen",
    bbox=dict(facecolor="white", ec="limegreen", lw=1),
    zorder=5,
)

ax.arrow(
    tplt_sup0[1],
    tplt_sup0[1],
    -np.pi + 0.2,
    0,
    ec="firebrick",
    fc="firebrick",
    width=0.01,
    length_includes_head=True,
    head_width=0.2,
    head_length=0.2,
    zorder=5,
)
ax.text(
    tplt_sup0[1] - np.pi / 2,
    tplt_sup0[1] + 0.3,
    "$-\\pi$",
    ha="center",
    va="bottom",
    fontsize=18,
    color="firebrick",
    bbox=dict(facecolor="none", ec="firebrick", lw=3, alpha=0.5),
    zorder=5,
)
ax.text(
    -2 * np.pi / 3 - 0.27,
    tplt_sup0[1] + np.pi / 2,
    "$\\theta_{\\rm vrai} = \\arctan(\\tan(\\theta))-\\pi$",
    ha="center",
    va="bottom",
    fontsize=12,
    color="firebrick",
    bbox=dict(facecolor="white", ec="firebrick", lw=2),
    zorder=5,
)

for mut in [-3, -1, 1, 3]:
    ax.axvline(mut * np.pi / 2, ls="--", color="k", lw=1, zorder=1)

ax.set_xlim(-3 * np.pi / 2, 3 * np.pi / 2)
ax.set_ylim(-3 * np.pi / 2, 3 * np.pi / 2)

ax.set_xlabel("$\\theta$", fontsize=15)
ax.xaxis.set_label_coords(1.05, 0.52)
ax.set_ylabel("$\\arctan(\\tan(\\theta))$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0.5, 1.02)

ax.set_yticks([])
ax.set_xticks([-3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2])
ax.set_xticklabels(
    [
        "$-\\frac{3\\pi}{2}$",
        "$-\\pi$",
        "$-\\frac{\\pi}{2}$",
        "$\\frac{\\pi}{2}$",
        "$\\pi$",
        "$\\frac{3\\pi}{2}$",
    ],
)

for axe in ["left", "bottom"]:
    ax.spines[axe].set_position("center")
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.get_xaxis_transform(), clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.get_yaxis_transform(), clip_on=False)

for tick in [0, 2, 3, 5]:
    ax.get_xticklabels()[tick].set_backgroundcolor("white")
    ax.get_xticklabels()[tick].set_zorder(3)

ax.legend(
    fontsize=10,
    ncol=3,
    columnspacing=2,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.15),
)

fig.savefig("./fig_atantan.pdf", bbox_inches="tight")
