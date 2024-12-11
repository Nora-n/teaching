import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

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
    preamble=r"\usepackage{xcolor}\usepackage{amsmath}\usepackage[detect-all,locale=FR,separate-uncertainty]{siunitx}[=v2]",
)

BrO3_0: float = 1.0e-3  # mol.L^-1
Br_0: float = 1.4e-1  # mol.L^-1
H3O_0: float = 1.0e-1  # mol.L^-1

k: float = 26  # mol^-3.L^3.s^-1
a: int = 1
b: int = 1
c: int = 2
kapp: float = k * Br_0**b * H3O_0**c  # s^-1

################## Ordre 0

t_tab: np.ndarray = np.linspace(0, 4e1, 1000)  # s
xmin, xmax = [min(t_tab), max(t_tab)]

C_tab: np.ndarray = BrO3_0 * np.exp(-kapp * t_tab) * 1e3  # mmol.L^-1
ymin, ymax = [0, max(C_tab)]

t_scat = np.array([0, 0.2, 0.35, 0.5, 1, 1.9, 3.85]) * 1e1  # s
# xmin, xmax = [min(t_scat), max(t_scat)]

C_scat: np.ndarray = BrO3_0 * np.exp(-kapp * t_scat) * 1e3  # mmol.L^-1
# ymin, ymax = [0, max(C_scat)]

# print(f"t_scat = {t_scat}\nC_scat = {C_scat}")

a, b = np.polyfit(t_scat, C_scat, 1)
C_reg: np.ndarray = a * t_tab + b

fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t$ (s)", fontsize=15, clip_on=False)
ax.ticklabel_format(style="sci", scilimits=(-3, 2), axis="x")
ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="y")
ax.set_ylabel("$C(t)$ (mmol$\\cdot$L$^{-1}$)", fontsize=15)

ax.set_xticks(np.arange(0, 40, 1), minor=True)
ax.set_yticks(np.arange(0, 1.1, 0.1))

ax.tick_params(which="major", length=7)
ax.tick_params(which="minor", length=4)

ax.grid(lw=1)
ax.grid(which="minor", ls="--", lw=0.5)

ax.scatter(
    t_scat,
    C_scat,
    marker="+",
    s=100,
    color="orange",
    label="Données",
    clip_on=False,
    zorder=7,
)
ax.plot(
    t_tab,
    C_reg,
    color="cornflowerblue",
    label="Régression\n"
    + rf"\begin{{eqnarray*}}a &=& \SI{{{a:.3f}}}{{mmol.L^{{-1}}.s^{{-1}}}}\\b &=& \SI{{{b:.3f}}}{{mmol.L^{{-1}}}}\end{{eqnarray*}}",
)

ax.legend(fontsize=12)

fig.savefig("./c(t).pdf", bbox_inches="tight")

################## Ordre 1

lnC_scat: np.ndarray = np.log(C_scat)

a, b = np.polyfit(t_scat, lnC_scat, 1)
lnC_reg: np.ndarray = a * t_tab + b

fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t$ (s)", fontsize=15, clip_on=False)
ax.ticklabel_format(style="sci", scilimits=(-3, 2), axis="x")
ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="y")
ax.set_ylabel("$\\ln(C(t))$ (mmol$\\cdot$L$^{-1}$)", fontsize=15)

ax.set_xticks(np.arange(0, 40, 1), minor=True)
# ax.set_yticks(np.arange(0, 1.1, 0.1))

ax.tick_params(which="major", length=7)
ax.tick_params(which="minor", length=4)

ax.grid(lw=1)
ax.grid(which="minor", ls="--", lw=0.5)

ax.scatter(
    t_scat,
    lnC_scat,
    marker="+",
    s=100,
    color="orange",
    label="Données",
    clip_on=False,
    zorder=7,
)
ax.plot(
    t_tab,
    lnC_reg,
    color="cornflowerblue",
    label="Régression\n"
    + rf"\begin{{eqnarray*}}a &=& \SI{{{a:.3f}}}{{s^{{-1}}}}\\b &=& \SI{{{b:.3f}}}{{mmol.L^{{-1}}}}\end{{eqnarray*}}",
)

ax.legend(fontsize=12)

fig.savefig("./lnc(t).pdf", bbox_inches="tight")

################## Ordre 2

invC_scat: np.ndarray = 1 / C_scat

a, b = np.polyfit(t_scat, invC_scat, 1)
invC_reg: np.ndarray = a * t_tab + b

fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes((0.10, 0.10, 0.8, 0.8))

ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)

ax.set_xlabel("$t$ (s)", fontsize=15, clip_on=False)
ax.ticklabel_format(style="sci", scilimits=(-3, 2), axis="x")
ax.ticklabel_format(style="sci", scilimits=(-3, 4), axis="y")
ax.set_ylabel("$\\displaystyle\\frac{1}{C(t)}$ (mmol$^{-1}\\cdot$L)", fontsize=15)

ax.set_xticks(np.arange(0, 40, 1), minor=True)
# ax.set_yticks(np.arange(0, 1.1, 0.1))

ax.tick_params(which="major", length=7)
ax.tick_params(which="minor", length=4)

ax.grid(lw=1)
ax.grid(which="minor", ls="--", lw=0.5)

ax.scatter(
    t_scat,
    invC_scat,
    marker="+",
    s=100,
    color="orange",
    label="Données",
    clip_on=False,
    zorder=7,
)
ax.plot(
    t_tab,
    invC_reg,
    color="cornflowerblue",
    label="Régression\n"
    + rf"\begin{{eqnarray*}}a &=& \SI{{{a:.3f}}}{{mmol^{{-1}}.L.s^{{-1}}}}\\b &=& \SI{{{b:.3f}}}{{mmol^{{-1}}.L}}\end{{eqnarray*}}",
)

ax.legend(fontsize=12)

fig.savefig("./invc(t).pdf", bbox_inches="tight")
