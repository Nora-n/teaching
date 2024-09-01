import matplotlib.pyplot as plt
import numpy as np
from intersect import intersection
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "EB Garamond",
    "axes.labelsize": 'x-large',
    "xtick.labelsize": 'x-large',
    "ytick.labelsize": 'x-large'})
plt.rcParams['figure.facecolor'] = 'w'

P0 = 1e5                        # Pa
V = 36                          # m^3
Tc = 292                        # K
C_v = 5*P0*V/(2*Tc)             # J.K^-1
gtoit = 0.50                    # W.m^-2.K^-1
gmur = 2.90                     # W.m^-2.K^-1
S = 12                          # m^2
Text = 283                      # K
Pc = (gtoit + gmur)*S*(Tc-Text)
tau = C_v/((gtoit+gmur)*S)
tau_h = tau/3600

def Tint_coupe(t):
    return(Text + (Tc-Text)*np.exp(-t/tau))
def Tint_coupe_h(t):
    return(Text + (Tc-Text)*np.exp(-t/tau_h))

xmin:int = 0
t1:int = 3 # h
Npts:int = 10000

t1_list:np.ndarray = np.linspace(xmin, t1, Npts)
Tint_coupe_list:np.ndarray = Tint_coupe(t1_list)
Tint_coupe_hlist:np.ndarray = Tint_coupe_h(t1_list)

fig = plt.figure(figsize=(5, 3))
ax = fig.add_axes((0.1, 0.12, 0.90, 0.8))

ax.plot(t1_list, Tint_coupe_hlist,
        lw=2, color='orange',
        label='Arrêt complet chauffage')
ax.plot([0,tau_h],[Tc,Text],
        ls='--', c='cornflowerblue',
        label=r'$\tau$')

ax.set_xlabel(r'$\tau$ (h)', x=1, ha='right', va='top')
ax.set_ylabel(r'$T_{\rm int}$ (K)', y=1.05, rotation=0, ha='left')

ax.set_xlim(left=0)
ax.set_ylim(bottom=Text)

ax.legend(fontsize='x-large')
ax.spines[['right', 'top']].set_visible(False)
ax.plot(0, 1, '^k', transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, '>k', transform=ax.transAxes, clip_on=False)

fig.savefig('E7_eqdiff.pdf', bbox_inches="tight")

#####

Pmax = 2.0e3 # W

def Tint_chauffe(t:float) -> float:
    return(Text + Pmax/((gtoit+gmur)*S)*(1-np.exp(-t/tau)))
def Tint_chauffe_h(t:float) -> float:
    return(Text + Pmax/((gtoit+gmur)*S)*(1-np.exp(-t/tau_h)))

xmin:int = 0
xmax:int = 1 # h
Npts:int = 10000

t_list:np.ndarray = np.linspace(xmin, xmax, Npts)
Tint_chauffe_list:np.ndarray = Tint_chauffe(t_list)
Tint_chauffe_hlist:np.ndarray = Tint_chauffe_h(t_list)

fig = plt.figure(figsize=(5, 3))
ax = fig.add_axes((0.1, 0.12, 0.90, 0.8))

ax.plot(t_list, Tint_chauffe_hlist,
        lw=2, color='orange',
        label='Relance du chauffage')
ax.plot([0,tau_h],[Text,max(Tint_chauffe_hlist)],
        ls='--', c='cornflowerblue',
        label=r'$\tau$')
# ax.axhline(Tc, ls=':', c='k')

# intersection
t2 = tau*np.log(Pmax/(Pmax-Pc))/3600
ax.plot([0,t2,t2],[Tc, Tc,Text],
        ls='--', c='k',
        label=fr'$t_2 =$ {t2*60:.1f} min')

ax.set_xlabel(r'$\tau$ (h)', x=1, ha='right', va='top')
ax.set_ylabel(r'$T_{\rm int}$ (K)', y=1.05, rotation=0, ha='left')

ax.set_xlim(left=0)
ax.set_ylim(bottom=Text)

ax.legend(fontsize='x-large')
ax.spines[['right', 'top']].set_visible(False)
ax.plot(0, 1, '^k', transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, '>k', transform=ax.transAxes, clip_on=False)

fig.savefig('E7_eqdiff_rechauffe.pdf', bbox_inches="tight")

# Combine
def Tint_chauffe_court(t):
    return(Text +
        (Tc-Text)*((Pmax/Pc)+np.exp(-t/tau)*(1-(Pmax/Pc)*np.exp(t1/tau))))
def Tint_chauffe_court_h(t):
    return(Text +
        (Tc-Text)*((Pmax/Pc)+np.exp(-t/tau_h)*(1-(Pmax/Pc)*np.exp(t1h/tau_h))))

def t2func(t1):
    return(tau*np.log((Pc-Pmax*np.exp(t1/tau))/(Pc-Pmax))) # s
def E_continu(t1):
    return(Pc*t2func(t1))
def E_rechauffe(t1):
    return(Pmax*(t2func(t1)-t1))

t1_test = np.linspace(0, 3600, Npts)

fig = plt.figure(figsize=(5, 3))
ax = fig.add_axes((0.1, 0.12, 0.90, 0.8))

ax.plot(t1_test, E_continu(t1_test),
        color='orange',
        label=r'Chauffage continu : $\mathcal{E} = \mathcal{P}_c\times t_2$')
ax.plot(t1_test, E_rechauffe(t1_test),
        color='firebrick',
        label=r'Interruption puis chauffage max : $\mathcal{E} = \mathcal{P}_{c,\rm max}\times(t_2-t_1)$')

# intersection
# ax.plot([0,t2,t2],[Tc, Tc, Text],
#         ls='--', c='k',
#         label=fr'$t_2 =$ {t2*60:.1f} min')

ax.set_xlabel(r'$t_1$ (s)', x=1, ha='right', va='top')
ax.set_ylabel(r'$\mathcal{E}$ (J)', y=1.05, rotation=0, ha='left')

ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

ax.legend(fontsize='15', bbox_to_anchor=[0.5, 1.2], loc='lower center')
ax.spines[['right', 'top']].set_visible(False)
ax.plot(0, 1, '^k', transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, '>k', transform=ax.transAxes, clip_on=False)

fig.savefig('E7_solve_t1_egal.pdf', bbox_inches="tight")

t1h = 0.5 # h
t1 = t1h*3600 # s
t1_list:np.ndarray = np.linspace(xmin, t1, Npts) # s
t1_hlist:np.ndarray = np.linspace(xmin, t1h, Npts) # h
Tint_coupe_list:np.ndarray = Tint_coupe(t1_list)
Tint_coupe_hlist:np.ndarray = Tint_coupe_h(t1_hlist)

t2 = tau*np.log((Pc-Pmax*np.exp(t1/tau))/(Pc-Pmax)) # s
t2h = t2/3600 # h
t2_list:np.ndarray = np.linspace(t1, t2, Npts) # s
t2_hlist:np.ndarray = np.linspace(t1h, t2h, Npts) # h
Tint_chauffe_court_list = Tint_chauffe_court(t2_list)
Tint_chauffe_court_hlist = Tint_chauffe_court_h(t2_hlist)

tmax_list = np.linspace(t2, t2+600, Npts) # s
tmax_hlist = np.linspace(t2h, t2h+600/3600, Npts) # h

fig = plt.figure(figsize=(5, 3))
ax = fig.add_axes((0.1, 0.12, 0.90, 0.8))

ax.plot(t1_hlist, Tint_coupe_hlist,
        lw=2, color='orange',
        label='Arrêt du chauffage')
ax.plot(t2_hlist, Tint_chauffe_court_hlist,
        lw=2, color='firebrick',
        label=r'Relance du chauffage à $\mathcal{P}_{c,\rm max}$')
ax.plot(tmax_hlist, Tc*np.ones(Npts),
        lw=2, color='pink',
        label=r'Chauffage à $\mathcal{P}_c$')
# ax.plot(t2_hlist, Tint_chauffe_court_hlist,
#         lw=2, color='firebrick',
#         label='Relance du chauffage')
# ax.plot([0,tau_h],[Text,max(Tint_chauffe_hlist)],
#         ls='--', c='cornflowerblue',
#         label=r'$\tau$')
# ax.axhline(Tc, ls=':', c='k')

# intersection
# ax.plot([0,t2,t2],[Tc, Tc, Text],
#         ls='--', c='k',
#         label=fr'$t_2 =$ {t2*60:.1f} min')

ax.set_xlabel(r'$\tau$ (h)', x=1, ha='right', va='top')
ax.set_ylabel(r'$T_{\rm int}$ (K)', y=1.05, rotation=0, ha='left')

ax.set_xlim(left=0)
ax.set_ylim(bottom=Text)

ax.legend(fontsize='x-large')
ax.spines[['right', 'top']].set_visible(False)
ax.plot(0, 1, '^k', transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, '>k', transform=ax.transAxes, clip_on=False)

ax.set_title(fr'$t_1 =$ {t1h*60} min, $\Delta{{t}}_{{12}} =$ {(t2h-t1h)*60:.2f} min',
             fontsize=20)

fig.savefig('E7_eqdiff_rechauffe_court.pdf', bbox_inches="tight")

