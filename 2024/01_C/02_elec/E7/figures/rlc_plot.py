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

wlist = np.linspace(0, 2 * w0, 1000)
xmin, xmax = [min(wlist), max(wlist)]


def Uc(w, Q=Q):
    x = w / w0
    return 1 / (1 - x**2 + 1j * x / Q)


fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

Qlist = [0.6, 1.5, 3]
ucls = ["firebrick", "limegreen", "cornflowerblue"]

ampl_dict = {Q: np.abs(Uc(wlist, Q=Q)) for Q in Qlist}

ymin, ymax = [0, 3.5]

ax.axvline(w0, ls="--", lw=1.5, color="black")

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
ax.xaxis.set_label_coords(0.90, -0.02)
ax.set_ylabel("$U_C/E_0$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([wr, w0])
ax.set_xticklabels(["$\\omega_r$", "$\\omega_0$"])
ax.set_yticks([0, 1, max(ampl_dict[Qlist[1]]), max(ampl_dict[Qlist[2]])])

ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

fig.savefig("./rlc_Uc_ampl_stud.pdf", bbox_inches="tight")

for Q, cl in zip(Qlist, ucls):
    ax.plot(wlist, ampl_dict[Q], color=cl, label=f"$Q = {Q}$")

Qspace = np.linspace(1.1 / np.sqrt(2), 3.5, 100)
wrspace = w0 * np.sqrt(Qspace**2 - 0.5) / (Qspace)
Uspace = Qspace / (np.sqrt(1 - 1 / (4 * Qspace**2)))

ax.plot(wrspace, Uspace, ls=":", lw=1, color="black", label="$U_{\\mathrm{max}}(Q)$")

ax.legend(fontsize=15)

fig.savefig("./rlc_Uc_ampl_prof.pdf", bbox_inches="tight")

################### ARGUMENT ###################

# wlist = np.linspace(0, 5 * wc, 1000)
# xmin, xmax = [min(wlist), max(wlist)]

fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "top"]:
    # ax.spines[axe].set_position("center")
    ax.spines[axe].set_linewidth(2)

for axe in ["bottom", "right"]:
    ax.spines[axe].set_visible(False)

# wloglist = np.logspace(2, 6, 10000)
# xmin, xmax = [min(wloglist), max(wloglist)]

acls = ucls
arg_dict = {Q: np.angle(Uc(wlist, Q=Q)) for Q in Qlist}
ymin, ymax = [-1.03 * np.pi, 0]

# ax.axhline(0, ls="--", color="black")
ax.axhline(-np.pi, ls="--", color="black")

ax.set_xlim(xmin, xmax)
# ax.set_xscale("log")
ax.set_ylim(ymin, ymax)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
ax.xaxis.set_label_coords(0.90, 1.07)
ax.set_ylabel("$\\varphi(\\omega)~[\\mathrm{rad}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

# ax.xaxis.set_major_locator(plt.FixedLocator([1e3, 1e4, 1e5, 1e6]))

ax.set_xticks([wr, w0])
ax.set_xticklabels(["$\\omega_r$", "$\\omega_0$"])
ax.set_yticks([-np.pi * (k / 4) for k in range(4, -1, -1)])
ax.set_yticklabels(
    [
        "$-\\displaystyle\\pi$",
        "$-\\displaystyle\\frac{3\\pi}{4}$",
        "$-\\displaystyle\\frac{\\pi}{2}$",
        "$-\\displaystyle\\frac{\\pi}{4}$",
        0.0,
    ],
)

# ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.tick_params(
    which="both",
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False,
)
ax.tick_params(which="major", length=7)
# ax.tick_params(which="minor", length=4)

ax.grid()
ax.grid(which="minor", ls="--")

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 1, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

fig.savefig("./rlc_Uc_arg_stud.pdf", bbox_inches="tight")

for Q, cl in zip(Qlist, acls):
    ax.plot(wlist, arg_dict[Q], color=cl, label=f"$Q = {Q}$")

ax.plot([0, w0], [-np.pi / 2, -np.pi / 2], ls="--", lw=1, color="black")
ax.plot([w0, w0], [0, -np.pi / 2], ls="--", lw=1, color="black")

ax.legend(fontsize=15)

fig.savefig("./rlc_Uc_arg_prof.pdf", bbox_inches="tight")

## INTENSITY

################### AMPLITUDE ###################


def I(w, Q=Q):
    x = w / w0
    return 1 / (1 + 1j * Q * (x - 1 / x))


wlist = np.linspace(1e-3, 2 * w0, 1000)
xmin, xmax = [min(wlist), max(wlist)]

fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    ax.spines[axe].set_linewidth(2)

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

Qlist = [0.6, 1.5, 3]
ucls = ["firebrick", "limegreen", "cornflowerblue"]

ampl_dict = {Q: np.abs(I(wlist, Q=Q)) for Q in Qlist}

ymin, ymax = [0, 1]

ax.axvline(w0, ls="--", lw=1.5, color="black")

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
ax.xaxis.set_label_coords(0.90, -0.02)
ax.set_ylabel("$\\frac{I}{E_0/R}$", fontsize=15, rotation=0, clip_on=False)
ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks([w0])
ax.set_xticklabels(["$\\omega_0 = \\omega_r$"])
ax.set_yticks([0, 1])

# ax.yaxis.set_major_formatter(tck.FormatStrFormatter("%.1f"))

ax.grid()

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

fig.savefig("./rlc_I_ampl_stud.pdf", bbox_inches="tight")

for Q, cl in zip(Qlist, ucls):
    ax.plot(wlist, ampl_dict[Q], color=cl, label=f"$Q = {Q}$")

# Qspace = np.linspace(1.1 / np.sqrt(2), 3.5, 100)
# wrspace = w0 * np.sqrt(Qspace**2 - 0.5) / (Qspace)
# Uspace = Qspace / (np.sqrt(1 - 1 / (4 * Qspace**2)))
#
# ax.plot(wrspace, Uspace, ls=":", lw=1, color="black", label="$U_{\\mathrm{max}}(Q)$")

ax.legend(fontsize=15, loc="lower right")

fig.savefig("./rlc_I_ampl_prof.pdf", bbox_inches="tight")

################### ARGUMENT ###################

# wlist = np.linspace(0, 5 * wc, 1000)
# xmin, xmax = [min(wlist), max(wlist)]

fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

for axe in ["left", "bottom"]:
    # ax.spines[axe].set_position("center")
    ax.spines[axe].set_linewidth(2)

ax.spines["bottom"].set_position("center")

for axe in ["top", "right"]:
    ax.spines[axe].set_visible(False)

# wloglist = np.logspace(2, 6, 10000)
# xmin, xmax = [min(wloglist), max(wloglist)]

acls = ucls
arg_dict = {Q: np.angle(I(wlist, Q=Q)) for Q in Qlist}
ymin, ymax = [-1.03 * np.pi, 0]

ax.axhline(-np.pi / 2, ls="--", color="black")
ax.axhline(np.pi / 2, ls="--", color="black")

ax.set_xlim(xmin, xmax)
# ax.set_xscale("log")
# ax.set_ylim(ymin, ymax)

ax.set_xlabel(
    "$\\omega~[\\mathrm{rad}\\cdot\\mathrm{s}^{-1}]$", fontsize=15, clip_on=False
)
ax.xaxis.set_label_coords(0.90, 0.57)
ax.set_ylabel("$\\varphi(\\omega)~[\\mathrm{rad}]$", fontsize=15, rotation=0)
ax.yaxis.set_label_coords(0, 1.02)

# ax.xaxis.set_major_locator(plt.FixedLocator([1e3, 1e4, 1e5, 1e6]))

ax.set_xticks([w0])
ax.set_xticklabels(["$\\omega_0$"])
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
# ax.tick_params(which="minor", length=4)

ax.grid()
ax.grid(which="minor", ls="--")

ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
ax.plot(1, 0.5, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

fig.savefig("./rlc_I_arg_stud.pdf", bbox_inches="tight")

for Q, cl in zip(Qlist, acls):
    ax.plot(wlist, arg_dict[Q], color=cl, label=f"$Q = {Q}$")

# ax.plot([0, w0], [-np.pi / 2, -np.pi / 2], ls="--", lw=1, color="black")
# ax.plot([w0, w0], [0, -np.pi / 2], ls="--", lw=1, color="black")

ax.legend(fontsize=15)

fig.savefig("./rlc_I_arg_prof.pdf", bbox_inches="tight")
