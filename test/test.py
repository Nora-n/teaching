import numpy as np
import matplotlib.pyplot as plt

# TP 18
# m = 10.4e-3    # kg
# tau = 73.5e-3  # s
# R = 1.0e-2     # m
# eta = m/(6*np.pi*tau*R)
# print(f'\\eta = {eta}')

# TD M7
# G = 6.67e-11 # SI
# M = 5.97e24  # kg
# r2 = 42200e3 # m
# r1 = 7500e3  # m
# v2 = np.sqrt(G*M/r2)
# ve2 = np.sqrt(2*G*M*r1/(r2*(r1+r2)))
# Dva = v2-ve2
# print(f'v_2 = {v2:.1f}, v_e2 = {ve2:.1f}, D v_A = {Dva:.1f}')
# v1 = np.sqrt(G*M/r1)
# ve1 = np.sqrt(2*G*M*r2/(r1*(r1+r2)))
# Dvp = ve1-v1
# print(f'v_1 = {v1:.1f}, v_e1 = {ve1:.1f}, D v_P = {Dvp:.1f}')
# # Wpp = 17e9 # J
# # m = 2*Wpp/(ve1**2-v1**2)
# m = 1000  # kg
# print(f'm = {m:.2e} kg')
# Wp_v = 0.5*m*(ve1**2 - v1**2)
# print(f'Wp_v = {Wp_v/1e9:.0f} GJ')
# Wp = G*m*M*(r2-r1)/(2*r1*(r1+r2))
# print(f'Wp = {Wp/1e9:.0f} GJ')
# Wa = (G*M*m*(r2-r1))/(2*r2*(r1+r2))
# print(f'Wa = {Wa/1e9:.1f} GJ')

# M7
# Tsid = 23*3600+56*60+4
# w_sid = 2*np.pi/(Tsid)
# print(f'w_sid = {w_sid:.2e} rad.s^-1')

# DS06
# B = 1.0 # T
# eSm = 2e11 # SI
# a = 1.0e-3 # m
# v = 2.0e8  # m.s^-1
# Dt = a*B*eSm/v
# print(f'Delta\\th = {Dt} rad = {Dt*180/np.pi}°')

# TDM8
# T = 4.1 # s
# L = 3.0 # m
# d = 4.5 # m
# m = 300 # kg
# mtot = 2.3e3 # kg
# g = 9.81 # m.s^-2
# J = T**2/(4*np.pi**2)*mtot*g*d - m*L**2/3
# print(f"J = {J:.1e} kg.m²")

# TP17
# m = 190e-3                           # kg
# g = 9.81                             # m.s^-2
# l = 45e-2                            # m
# ul = 0.25e-2/np.sqrt(3)              # m
# a_theo = m*g*l/2                     # J.rad^-2
# a_expe = 0.406                       # J.rad^-2
# ua_expe = m*g*ul/2                   # m
# En = abs(a_theo - a_expe)/(ua_expe) # R
# print(f'a_theo = {a_theo:.3f} ; a_expe = {a_expe:.3f}±{ua_expe:.3f} ; En = {En}')

# TDC4-C5
# Ks = 10**-25.2
# K1 = 10**-2.1
# K2 = 10**-5
# K3 = 10**-9.5
# Ke = 10**-14
# K5 = Ks*K1*K2/(Ke**2)
# # print(f'K5 = {K5}, s2 = {10**-4.3}')
# pK5 = -np.log10(K5)
# pKA3 = -np.log10(K3)
# # print(f'log $s$ - pH = {-pK5 - pKA3}')
#
# def s(h):
#     return(K5*(h**2/(K1*K3) + h/K2 + 1 + K3/h))
# def logs(ph):
#     hlocal = 10**-ph
#     return np.log10(K5*(hlocal**2/(K1*K3) + hlocal/K2 + 1 + K3/hlocal))
#
# phlist = np.linspace(2, 14, 500)
# fig = plt.figure(figsize=(7,6))
# # plt.loglog(hlist, s(hlist))
# plt.plot(phlist, logs(phlist))
# plt.grid()
# plt.xlim(0,14)
# plt.ylim(top=0)
# plt.show()

# DS07 metronome
# m = 20e-3  # kg
# M = 200e-3 # kg
# g = 10     # m.s^-2
# R = 1.5e-2 # m
# ell = 2e-2 # m
# T0 = 1.2   # s
# D = m**2*g*T0**2/(16*np.pi**4) - 4*m*(2/5*M*R**2 + M*ell**2 -
#     T0**2*M*g*ell/(4*np.pi**2))
#
# xp = -0.5*g*T0**2/(4*np.pi**2) + np.sqrt(D)/(2*m)
# xm = -0.5*g*T0**2/(4*np.pi**2) - np.sqrt(D)/(2*m)
# print(f'x_+ = {xp*1e2:.2f} cm et x_- = {xm*1e2:.2f}')
# T0 = 1    # s
# xp = -0.5*g*T0**2/(4*np.pi**2) + np.sqrt(D)/(2*m)
# D = m**2*g*T0**2/(16*np.pi**4) - 4*m*(2/5*M*R**2 + M*ell**2 -
#     T0**2*M*g*ell/(4*np.pi**2))
# print(f'x_+ allegro = {xp*1e2:.2f} cm')
# xp = ((g*T0**2)/(8*np.pi**2))*(
#     -1 + np.sqrt(
#     1 -
#             ((64*M*np.pi**4)/(m*g**2*T0**4))*(ell**2 + 2/5*R**2) +
#         ((16*M*np.pi**2)/(m*g*T0**2))*ell)
# )
# print(f'x_+ direct = {xp*1e2:.2f} cm')
# RT = 6370e3  # km
# h = 800e3    # m
# G = 6.67e-11 # m^3kg^-1s^-1
# MT = 5.97e24 # kg
# T = 2*np.pi*np.sqrt((RT+h)**3/(G*MT))
# print(f'T = {T:.2e}')
# v = np.sqrt((G*MT)/(RT+h))
# print(f'v = {v:.2e}')

# C7
# ct = 1
# pke = 14
# pks = 33.5
# pbeta4 = -35
# pkr = pks + pbeta4
# ph = pkr + pke + np.log10(ct)
# print(f'pH = {ph}')

# TDT3 exo chambre
# P0 = 1e5  # Pa
# V = 36  # m^3
# Tc = 292  # K
# C_v = 5 * P0 * V / (2 * Tc)
# print(f"C_v = {C_v:.2e} J.K^-1")
# gtoit = 0.50  # W.m^-2.K-1
# gmur = 2.90  # W.m^-2.K-1
# S = 12  # m^2
# Text = 283  # K
# Pc = (gtoit + gmur) * S * (Tc - Text)
# print(f"Pc = {Pc:.1e} W")
# tau = C_v / ((gtoit + gmur) * S)
# print(f"\\tau = {tau:.1e} s")
# tau_m = tau / 60
# print(f"\\tau_m = {tau_m:.1f} min")
#
# Pmax = 2e3  # W
# conv_euro = 0.27 / (1e3 * 3600)
#
# t2 = tau * np.log(Pmax / (Pmax - Pc))
# print(f"t2 = {t2:.1f} s")
#
# t_garde = 3 * 3600 + t2  # s
# print(f"t_garde = {t_garde:.2e} s")
# Q_garde = Pc * t_garde  # J
# print(f"Q_garde = {Q_garde:.2e} J")
# Q_garde_euro = Q_garde * conv_euro  # €
# print(f"Q_garde_euro = {Q_garde_euro:.2e} €")
#
# Q_rechauffe = Pmax * t2  # J
# print(f"Q_rechauffe = {Q_rechauffe:.2e} J")
# Q_rechauffe_euro = Q_rechauffe * conv_euro  # #
# print(f"Q_rechauffe_euro = {Q_rechauffe_euro:.2e} €")
#
# t_egal = t2 * (Pmax / Pc - 1)
# print(f"t_egal = {t_egal/60:.2e} min")

# TDN1 Taylor
# R = 70  # m
# t = 5.0e-3  # s
# rho = 1.2  # kg.m⁻³
# E = R**5 * t**-2 * rho
# print(f"E = {E:.2e} J")
# conv = 4.18e9  # J/T
# E_david = 7.7e13  # J
# print(f"E en T TNT = {E/conv:.2e} T de TNT")
# print(f"E_david en T TNT = {E_david/conv:.2e} T de TNT")

# TDO3 œil réduit
# OA = -1.0  # m
# OAp = 22.3e-3  # m
# V = (OA - OAp) / (OAp * OA)
# print(f"V = {V:.2e} m⁻¹")
# gamma = OAp / OA
# print(f"gamma = {gamma:.2e}")
# AB = 10  # cm
# ABp = gamma * AB
# print(f"A'B' = {ABp:.2f} cm")

# TDO3 vidéoproj
# OAp = 4.0  # m
# OFp = 5.0e-2  # m
# OA = (OAp * OFp) / (OFp - OAp)
# print(f"OA = {OA:.3f} m")

# DS03 2024 ammoniac rendement
# K = 2.8e-5
# C = 900 * np.sqrt(3 * K) + 4
# rdm_coeff = [C, -2 * C, C - 4]
#
# rdm_mano = 1-2/np.sqrt(C)
# print(rdm_mano)
#
# rdm_solv = np.roots(rdm_coeff)
# print(rdm_solv)

# TDE5, dec log
# uinf = 3 # V
# u1 = 4.9 # V
# u2 = 3.3 # V
# dlt = 0.5*np.log((u1-uinf)/(u2-uinf))
# print(f"delta = {dlt:.2f}")
#
# T = 387e-6 # s
# lbd = dlt/T
# print(f"lambda = {lbd:.3e} s⁻¹")

# E7 test
# Qlist = np.linspace(1.1 / np.sqrt(2), 3, 10)
# xlist = np.sqrt(1 - 1 / (2 * Qlist**2))
# Ulist = Qlist / np.sqrt(1 - 1 / (4 * Qlist**2))
# plt.scatter(xlist, Ulist, s=100, c="firebrick")
# plt.scatter([1 for Q in Qlist], Qlist, s=100, c="cornflowerblue")
# plt.show()

# f(X) for demo résonance tension
Qlist = [0.6, 1 / np.sqrt(2), 1.1 / np.sqrt(2), 1.5, 3, 5]
xlist = np.linspace(0, 1.5, 100)
xrdict = {}
for Q in Qlist:
    if Q <= 1 / np.sqrt(2):
        xrdict[Q] = 0
    else:
        xrdict[Q] = np.sqrt(Q**2 - 0.5) / Q


def f(x: float, Q: float) -> float:
    X = x**2
    return (1 - X) ** 2 + X / (Q**2)


fdict = {Q: f(xlist, Q) for Q in Qlist}
ucls = ["firebrick", "orange", "limegreen", "cornflowerblue", "violet", "black"]

for Q, cl in zip(Qlist, ucls):
    plt.plot(xlist, fdict[Q], color=cl, label=f"$Q = {Q:.2f}$")
    plt.scatter(xrdict[Q], f(xrdict[Q], Q), color=cl, s=100)
    # print(f(xrdict[Q], Q))

plt.legend()
plt.show()


# TDE8
# def H(x):
#     return (-(x**2)) / (1 - x**2 + 3j * x)
#
#
# xlist = np.logspace(-2, 2, 100)
# plt.plot(xlist, np.angle(H(xlist)))
# plt.xscale("log")
# plt.show()
