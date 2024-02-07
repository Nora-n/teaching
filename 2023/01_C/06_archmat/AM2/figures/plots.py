import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'
plt.rc('text.latex',
       preamble=r'\usepackage[detect-all,locale=FR]{siunitx}[=v2]')

data = {"EL":
        np.array([r"CH$_4$", r"SiH$_4$", r"GeH$_4$", r"SnH$_4$"]),
        "N":
        np.array([2,3,4,5]),
        "TEB":
        np.array([-161.5,-112,-88.5,-52]),
        }

fig = plt.figure(figsize=(7,5))
rect = 0.1, 0.10, 0.8, 0.8
ax = fig.add_axes(rect)

ax.plot(data["N"], data["TEB"],
            marker="+",
            ms="20",
            lw=2,
            color="cornflowerblue",
            label="Données")
ax.set_xlabel("Période",fontsize=20)
ax.set_ylabel("$\\theta_{\\rm eb} (\\si{\\degreeCelsius})$",fontsize=20)

ax.set_xlim(1,5.3)
ax.set_xticks([1,2,3,4,5])

for i in range(len(data["EL"])):
    ax.text(data["N"][i]-0.15, data["TEB"][i], data["EL"][i],
            ha="right", va="center", fontsize=20)

ax.legend(fontsize=15)
# fig.savefig(f"./2023/01_C/06_archmat/AM2/figures/hydro_14.pdf",
#             bbox_inches="tight")

data = {
    "15": {
        "EL":
        np.array([r"NH$_3$", r"PH$_3$", r"AsH$_3$", r"SbH$_3$"]),
        "N":
        np.array([2,3,4,5]),
        "TEB":
        np.array([-33.34,-87.7,-62.5,-17]),
        "HA":
        np.array(["right", "center", "right", "left"]),
        "VA":
        np.array(["center", "top", "bottom", "center"]),
        "HO":
        np.array([-0.15, 0, -0.05, 0.15]),
        "VO":
        np.array([0, -5, 0, 0]),
     },
    "16": {
        "EL":
        np.array([r"H$_2$O", r"H$_2$S", r"H$_2$Se", r"H$_2$Te"]),
        "N":
        np.array([2,3,4,5]),
        "TEB":
        np.array([100,-60,-41.25,-2]),
        "HA":
        np.array(["right", "left", "center", "left"]),
        "VA":
        np.array(["center", "bottom", "bottom", "center"]),
        "HO":
        np.array([-0.15, 0, 0, 0.15]),
        "VO":
        np.array([0, 5, 5, 0]),
     },
    "17": {
        "EL":
        np.array([r"HF", r"HCl", r"HBr", r"HI"]),
        "N":
        np.array([2,3,4,5]),
        "TEB":
        np.array([19.5,-85,-67,-35]),
        "HA":
        np.array(["right", "left", "center", "left"]),
        "VA":
        np.array(["center", "bottom", "top", "center"]),
        "HO":
        np.array([-0.15, 0, 0, 0.15]),
        "VO":
        np.array([0, 5, -5, 0]),
     },
}

colors = {
    "15": "cornflowerblue",
    "16": "limegreen",
    "17": "orange"
}

data_att = {
    "15": {
        "EL":
        np.array([r"?", r"PH$_3$"]),
        "N":
        np.array([2,3]),
        "TEB":
        np.array([-130,-87.7]),
        "HA":
        np.array(["right", "center"]),
        "VA":
        np.array(["center", "top"]),
        "HO":
        np.array([-0.15, 0]),
        "VO":
        np.array([0, -5]),
     },
    "16": {
        "EL":
        np.array([r"?", r"H$_2$S"]),
        "N":
        np.array([2,3]),
        "TEB":
        np.array([-75,-60]),
        "HA":
        np.array(["right", "left"]),
        "VA":
        np.array(["center", "bottom"]),
        "HO":
        np.array([-0.15, 0]),
        "VO":
        np.array([0, 5]),
     },
    "17": {
        "EL":
        np.array([r"?", r"HCl"]),
        "N":
        np.array([2,3]),
        "TEB":
        np.array([-110,-85]),
        "HA":
        np.array(["right", "left"]),
        "VA":
        np.array(["center", "bottom"]),
        "HO":
        np.array([-0.15, 0]),
        "VO":
        np.array([0, 5]),
     },
}
fig = plt.figure(figsize=(7,5))
rect = 0.1, 0.10, 0.8, 0.8
ax = fig.add_axes(rect)

for k in data.keys():
    dta = data[k]
    dtat = data_att[k]
    ax.plot(dta["N"], dta["TEB"],
                marker="+",
                ms="20",
                lw=2,
                color=colors[k],
                label=f"Colonne {k}")
    ax.set_xlabel("Période",fontsize=20)
    ax.set_ylabel("$\\theta_{\\rm eb} (\\si{\\degreeCelsius})$",fontsize=20)

    for i in range(len(dta["EL"])):
        ax.text(dta["N"][i]+dta["HO"][i], dta["TEB"][i]+dta["VO"][i],
                dta["EL"][i],
                ha=dta["HA"][i], va=dta["VA"][i], fontsize=20)

    ax.plot(dtat["N"], dtat["TEB"],
            marker="+",
            ms="20",
            lw=2,
            ls="--",
            color=colors[k])
    for i in range(len(dtat["EL"])):
        ax.text(dtat["N"][i]+dtat["HO"][i], dtat["TEB"][i]+dtat["VO"][i],
                dtat["EL"][i],
                ha=dtat["HA"][i], va=dtat["VA"][i], fontsize=20)

    ax.legend(fontsize=15)

ax.set_xlim(1,5.7)
ax.set_xticks([1,2,3,4,5])
ax.set_ylim(bottom=-150)

# fig.savefig(f"./2023/01_C/06_archmat/AM2/figures/LH.pdf",
#             bbox_inches="tight")

# Exercice VII TD AM1-2

data = {
    "14": {"EL":
        np.array([r"CH$_4$", r"SiH$_4$", r"GeH$_4$", r"SnH$_4$"]),
        "MM":
        np.array([16.04, 32.12, 76.62, 122.71]),
        "TEB":
        np.array([-161.5,-112,-88.5,-52]),
        "HA":
        np.array(["center", "left", "center", "center"]),
        "VA":
        np.array(["top", "top", "top", "top"]),
        "HO":
        np.array([0, 0, 0, 0]),
        "VO":
        np.array([-5, -5, -5, -5]),
        },
    "17": {
        "EL":
        np.array([r"HF", r"HCl", r"HBr", r"HI"]),
        "MM":
        np.array([20.01, 36.46, 80.91, 127.91]),
        "TEB":
        np.array([19.5,-85,-67,-35]),
        "HA":
        np.array(["center", "left", "center", "center"]),
        "VA":
        np.array(["bottom", "bottom", "bottom", "bottom"]),
        "HO":
        np.array([0, 0, 0, 0]),
        "VO":
        np.array([5, 5, 5, 5]),
     },
}

colors = {
    "14": "cornflowerblue",
    "17": "orange",
}

fig = plt.figure(figsize=(7,5))
rect = 0.1, 0.10, 0.8, 0.8
ax = fig.add_axes(rect)
ax.grid()

for k in data.keys():
    dta = data[k]
    ax.plot(dta["MM"], dta["TEB"],
                marker="+",
                ms="20",
                lw=2,
                color=colors[k],
                label=f"Colonne {k}")
    ax.set_xlabel("Masse molaire ($\\si{g.mol^{-1}}$)",fontsize=20)
    ax.set_ylabel("$\\theta_{\\rm eb} (\\si{\\degreeCelsius})$",fontsize=20)

    for i in range(len(dta["EL"])):
        ax.text(dta["MM"][i]+dta["HO"][i], dta["TEB"][i]+dta["VO"][i],
                dta["EL"][i],
                ha=dta["HA"][i], va=dta["VA"][i], fontsize=20)

    ax.legend(fontsize=15)

ax.set_xlim(0, 140)
ax.set_ylim(-180, 40)

fig.savefig(f"./2023/02_TD/06_archmat/AM1-AM2/figures/teb_hydro.pdf",
            bbox_inches="tight")
