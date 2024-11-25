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

mpl.rc(
    "text.latex",
    preamble=r"\usepackage{xcolor}\usepackage{amsmath}\usepackage{amssymb}\usepackage{physics}",
)

################### AMPLITUDE ###################

E0 = 5  # V
R = 5000  # O
C = 0.10e-6  # F
C0 = 0.05e-6  # F
L = 9.9e-2  # H
f = 1.2e3  # Hz
w = 2 * np.pi * f  # rad.s^-1
w0 = 1 / np.sqrt(L * C)
w0p = np.sqrt((C + C0) / (L * C * C0))

# print(w0, w0p)

wlist = np.linspace(1, 10 * w0p, 10000)
xmin, xmax = [min(wlist), max(wlist)]


def Zu(w, C0=C0, C=C, L=L):
    return 1j * (L * C * w**2 - 1) / (w * ((C + C0) - L * C * C0 * w**2))


def ZuR(w, C0=C0, C=C, L=L, R=R):
    return (1 - L * C * w**2 + 1j * R * C * w) / (
        -R * C0 * C * w + 1j * ((C0 + C) * w - L * C0 * C * w**2)
    )


fig = plt.figure(figsize=(5, 5), constrained_layout=True)
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ampl_list = np.abs(Zu(wlist))
ampr_list = np.abs(ZuR(wlist))
# ymin, ymax = [min(ampl_list), max(ampl_list)]

# print(ampl_list)

ax.set_xlim(xmin, xmax)
ax.set_ylim(0, 1e4)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
# ax.xaxis.set_label_coords(1.05, 0.02)
ax.set_ylabel("$\\abs{\\underline{Z}}~[\\Omega]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([w0, w0p])
ax.set_xticklabels(
    [
        "$\\omega_0$",
        "$\\omega_0'$",
    ],
)
# ax.set_yticks([])
# ax.set_yticklabels(
#     [
#         "$\\displaystyle-\\frac{\\pi}{2}$",
#         -1.0,
#         -0.5,
#         0.0,
#         0.5,
#         1.0,
#         "$\\displaystyle\\frac{\\pi}{2}$",
#     ],
# )

# ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

# fig.savefig("./rcPl_Ul_ampl_stud.pdf", bbox_inches="tight")

ax.plot(wlist, ampl_list, color="firebrick")
ax.plot(wlist, ampr_list, color="cornflowerblue")
ax.axvline(w0p, ls="--", lw=1, color="black")

fig.savefig("./quartz_ampl.pdf", bbox_inches="tight")

#################### ARGUMENT ###################
#
## wlist = np.linspace(0, 5 * wc, 1000)
## xmin, xmax = [min(wlist), max(wlist)]
#
# fig = plt.figure(figsize=(5, 5), constrained_layout=True)
# ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))
#
# for axe in ["left", "bottom"]:
#    # ax.spines[axe].set_position("center")
#    ax.spines[axe].set_linewidth(2)
#
# ax.spines["bottom"].set_position("center")
#
# for axe in ["top", "right"]:
#    ax.spines[axe].set_visible(False)
#
# wloglist = np.logspace(2, 6, 10000)
# xmin, xmax = [min(wloglist), max(wloglist)]
#
# arg_list = np.angle(Ul(wloglist))
# ymin, ymax = [min(arg_list), max(arg_list)]
#
# ax.axhline(-np.pi / 2, ls="--", color="black")
# ax.axhline(np.pi / 2, ls="--", color="black")
#
# ax.set_xlim(xmin, xmax)
# ax.set_xscale("log")
## ax.set_ylim(-1.60, ymax + 0.07)
#
# ax.set_xlabel(
#    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
# )
# ax.xaxis.set_label_coords(0.90, 0.57)
# ax.set_ylabel("$\\varphi(\\omega)~[\\mathrm{rad}]$", fontsize=15, rotation=0)
# ax.yaxis.set_label_coords(0, 1.02)
#
# ax.xaxis.set_major_locator(plt.FixedLocator([1e3, 1e4, 1e5, 1e6]))
#
## ax.set_xticks(np.arange(2000, 10001, 2000))
# ax.set_yticks([-np.pi / 2, *np.arange(-1.0, 1.1, 0.5), np.pi / 2])
# ax.set_yticklabels(
#    [
#        "$\\displaystyle-\\frac{\\pi}{2}$",
#        -1.0,
#        -0.5,
#        0.0,
#        0.5,
#        1.0,
#        "$\\displaystyle\\frac{\\pi}{2}$",
#    ],
# )
#
## ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
# ax.tick_params(
#    which="both",
#    # top=True,
#    # labeltop=True,
#    # bottom=False,
#    # labelbottom=False,
# )
# ax.tick_params(which="major", length=7)
# ax.tick_params(which="minor", length=4)
#
# ax.grid()
# ax.grid(which="minor", ls="--")
#
# ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
# ax.plot(1, 0.5, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
#
## fig.savefig("./rcPl_Ul_arg_stud.pdf", bbox_inches="tight")
#
# ax.plot(wloglist, arg_list, color="limegreen")
#
# fig.savefig("./rcPl_Ul_arg_prof.pdf", bbox_inches="tight")
