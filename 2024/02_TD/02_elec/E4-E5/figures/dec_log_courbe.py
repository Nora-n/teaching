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

uinf = 3  # V
R1 = 1e3  # O
R2 = 50e3  # O
E0 = uinf * (R1 + R2) / R2  # V
print(f"$E$ = {E0:2f} V")
L = 500e-3  # H
lbd = 2.32e3  # s^-1
C = 1 / (2 * R2 * lbd - R1 * R2 / L)  # F
print(f"$C$ = {C:.2e} F")
# lbd = 0.5 * (1 / (R2 * C) + R1 / L)  # s^-1
# print(f"$\\lambda$ = {lbd:2e} s⁻¹")
w0 = np.sqrt((R1 + R2) / (R2 * L * C))  # rad.s^1
print(f"$\\omega_0$ = {w0:2e} rad.s⁻¹")
w = np.sqrt(w0**2 - lbd**2)
print(f"$\\omega$ = {w:2e} rad.s⁻¹")
T = 2 * np.pi / w  # s
print(f"$T$ = {T:3e} s")
# T = 600e-6  # s

tlist = np.linspace(-T, 3 * T, 1000)
xmin, xmax = [min(tlist), max(tlist)]


def ufunc(t):
    if t < 0:
        return 0
    else:
        return -uinf * (
            np.exp(-lbd * t) * (np.cos(w * t) + (lbd / w) * np.sin(w * t)) - 1
        )


u = np.vectorize(ufunc, otypes=[np.float64])

fig = plt.figure(figsize=(5, 2.5), constrained_layout=True)
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

# for axe in ["left", "bottom"]:
#     ax.spines[axe].set_linewidth(2)
#
# for axe in ["top", "right"]:
#     ax.spines[axe].set_visible(False)

u_list = u(tlist)
ymin, ymax = [min(u_list) - 1, 5]

ax.plot(tlist, u_list, color="firebrick")
# ax.axvline(Vlim, c="k", ls="--", lw=1)

ax.grid(visible=True, which="both")

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t$ (s)", fontsize=15, clip_on=False)
# ax.xaxis.set_label_coords(1.05, 0.02)
ax.set_ylabel("$u(t)$ (V)", fontsize=15)
# ax.yaxis.set_label_coords(0, 1.02)

ax.set_xticks(np.arange(-4e-4, 1.2e-3, 1e-4))
plt.setp(ax.get_xticklabels(), ha="right", rotation=45)
# lbls = ax.get_xticklabels()
# ax.set_xticklabels(lbls, rotation=45)
ax.set_yticks(np.arange(-1, 6, 0.5))
# ax.set_yticklabels(["$P_{\\mathrm{max}} = K^\\circ P^\\circ$"])
# ax.set_yticklabels(["$P_{\\mathrm{max}}$"])

ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="x")

# ax.plot(0, 1, "^k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)
# ax.plot(1, 0, ">k", lw=2, ms=5, transform=ax.transAxes, clip_on=False)

# plt.show()

fig.savefig("./dec_log_courbe.pdf", bbox_inches="tight")
