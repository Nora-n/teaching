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

H0 = 1 / 3
Q = 1 / 3
R = 1e4  # O
C = 10e-6  # F
w0 = 1 / (R * C)


wlist = np.linspace(1e-3, 5e3, 5000)
xmin, xmax = [min(wlist), max(wlist)]

wloglist = np.logspace(-2, 4, 5000)
xmin, xmax = [min(wloglist), max(wloglist)]


def H(w):
    x = w / w0
    return H0 / (1 + 1j * Q * (x - 1 / x))


fig = plt.figure(figsize=(5, 2.5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

ampl_list = np.abs(H(wloglist))
ymin, ymax = [min(ampl_list), max(ampl_list)]

ax.set_xlim(xmin, xmax)
ax.set_xscale("log")
ax.set_ylim(ymin, 0.35)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
# ax.xaxis.set_label_coords(1.05, 0.02)
ax.set_ylabel("$H_m(\\omega)$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

# ax.set_xticks(np.arange(1000, 5001, 1000))
# ax.set_xticks(np.arange(0, 5000, 100), minor=True)
# ax.set_xticklabels(["", "", 1000, "", "", *np.arange(2000, 5001, 1000)])

# ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.tick_params(
    which="both",
    # top=True,
    # labeltop=True,
    # bottom=False,
    # labelbottom=False,
)
ax.tick_params(which="major", length=7)
ax.tick_params(which="minor", length=4)

ax.grid(lw=1)
ax.grid(which="minor", ls="--", lw=0.5)

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

# fig.savefig("./rcl_Ul_ampl_stud.pdf", bbox_inches="tight")

ax.plot(wloglist, ampl_list, color="firebrick")

fig.savefig("./wien_ampl.pdf", bbox_inches="tight")

################### ARGUMENT ###################

# wlist = np.linspace(0, 5 * wc, 1000)
# xmin, xmax = [min(wlist), max(wlist)]

fig = plt.figure(figsize=(5, 2.5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    # ax.spines[axe].set_position("center")
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

# wloglist = np.logspace(1, 5, 5000)
# xmin, xmax = [min(wloglist), max(wloglist)]

arg_list = np.angle(H(wloglist))
ymin, ymax = [min(arg_list), max(arg_list)]

ax.axhline(-np.pi / 2, ls="--", color="black")
ax.axhline(np.pi / 2, ls="--", color="black")

ax.set_xlim(xmin, xmax)
ax.set_xscale("log")
# ax.set_ylim(-1.60, ymax + 0.07)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
# ax.xaxis.set_label_coords(0.90, 0.57)
ax.set_ylabel("$\\varphi(\\omega)~[\\mathrm{rad}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

# ax.xaxis.set_major_locator(plt.FixedLocator([1e1, 1e2, 1e3, 1e4, 1e5, 1e6]))

# ax.set_xticks(np.arange(1000, 5001, 1000))
# ax.set_xticks(np.arange(0, 5000, 100), minor=True)
# ax.set_xticklabels(["", "", 1000, "", "", *np.arange(2000, 5001, 1000)])

ax.set_yticks([np.pi * (k / 4) for k in range(-2, 3, 1)])
ax.set_yticklabels(
    [
        "$-\\displaystyle\\frac{\\pi}{2}$",
        "$-\\displaystyle\\frac{\\pi}{4}$",
        0.0,
        "$\\displaystyle\\frac{\\pi}{4}$",
        "$\\displaystyle\\frac{\\pi}{2}$",
    ],
)

# ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.tick_params(
    which="both",
    # top=True,
    # labeltop=True,
    # bottom=False,
    # labelbottom=False,
)
ax.tick_params(which="major", length=7)
ax.tick_params(which="minor", length=4)

ax.grid(lw=1)
ax.grid(which="minor", ls="--", lw=0.5)

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

# fig.savefig("./rcl_Ul_arg_stud.pdf", bbox_inches="tight")

ax.plot(wloglist, arg_list, color="limegreen")

fig.savefig("./wien_arg.pdf", bbox_inches="tight")

################## TIMESERIES ##################

# tlist = np.linspace(0, 4.5 * T, 1000)
# xmin, xmax = [min(tlist), max(tlist)]
#
#
# def ufunc(t):
#     return np.abs(Ul(w)) * np.cos(w * t + np.angle(Ul(w)))
#
#
# def efunc(t):
#     return E0 * np.cos(w * t)
#
#
# print(f"f = w/2pi = {w/(2*np.pi)}")
# print(f"U_m = {np.abs(Ul(w))}")
# print(f"phi = {np.angle(Ul(w))} et 2pi/3 = {phi}")
# print(f"u(0) = {ufunc(0)}")
#
# u = np.vectorize(ufunc, otypes=[np.float64])
# e = np.vectorize(efunc, otypes=[np.float64])
#
# fig = plt.figure(figsize=(7.5, 5))
# ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))
#
# # for axe in ["left", "bottom"]:
# #     ax.spines[axe].set_linewidth(2)
# #
# # for axe in ["top", "right"]:
# #     ax.spines[axe].set_visible(False)
#
# u_list = u(tlist)
# e_list = e(tlist)
# ymin, ymax = [min(e_list), max(e_list)]
#
# ax.plot(tlist, e_list, color="cornflowerblue", label="$e(t)$")
# ax.plot(tlist, u_list, ls="--", color="firebrick", label="$u(t)$")
# # ax.axvline(Vlim, c="k", ls="--", lw=1)
#
# ax.legend(loc="upper right", fontsize=15, framealpha=1)
#
# ax.grid(visible=True, which="both")
#
# ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)
#
# ax.set_xlabel("$t$ (s)", fontsize=15, clip_on=False)
# # ax.xaxis.set_label_coords(1.05, 0.02)
# ax.set_ylabel("tensions (V)", fontsize=15)
# # ax.yaxis.set_label_coords(0, 1.02)
#
# # ax.set_xticks(np.arange(-4e-4, 1.2e-3, 1e-4))
# # plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
# # lbls = ax.get_xticklabels()
# # ax.set_xticklabels(lbls, rotation=45)
# # ax.set_yticks(np.arange(-10, 10.1, 1))
# # ax.set_yticklabels(["$P_{\\mathrm{max}} = K^\\circ P^\\circ$"])
# # ax.set_yticklabels(["$P_{\\mathrm{max}}$"])
#
# ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="x")
#
# # ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
# # ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
#
# # plt.show()
#
# fig.savefig("./rcl_Ul_time.pdf", bbox_inches="tight")
