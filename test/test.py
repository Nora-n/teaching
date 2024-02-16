import numpy as np

# DS06
# rho = 2.7e3 # kg.m-3
# a = 20e-6   # m
# S = 5e-2    # m²
# k = 1000    # N.m⁻¹
# e = 3e-3    # m
# z0 = -e/100 # m
#
# T0 = 2*np.pi*np.sqrt(rho*a*S/k*((e+z0)/(e+3*z0)))
# print(f'T_0 = {T0:.2e}')

# DS06
# h = 4 # m
# n = 2.3
# alpha = h/(2*np.pi*n)
# print(f'\\alpha = \\SI{{{alpha:.2f}}}{{m.rad^{{-1}}}}')

# DS06 P2
m = 9.31e-31 # kg
g = 10.0     # m.s^-2
e = 1.6e-19  # C
v = 1e8      # m.s^-1
Bmin = m*g/(e*v) # T
print(f'Bmin = {Bmin:.2e} T')

# TP 18
# m = 10.4e-3    # kg
# rho = 970      # kg.m^-3
# tau1 = 160e-3  # s
# tau2 = 162e-3  # s
# tau = np.mean([tau1,tau2]) # s
# ec_tau = 10e-3  # s
# R = 1.0e-2     # m
# eta_exp = m/(6*np.pi*tau*R)
# ec_etaexp = eta_exp*ec_tau/tau
#
# kin_min = 332e-6    # m^2.s^-1
# kin_max = 362e-6    # m^2.s^-1
# eta_min = rho*kin_min  # cP
# eta_max = rho*kin_max  # cP
# eta_the = np.mean([eta_min, eta_max])
# ec_etat = (eta_max - eta_min)/(2*np.sqrt(3))
# print(f'$\\eta_{{\\rm cons}} = [{eta_min:.2f}, {eta_max:.2f}] Pa.s$')
# print(f'\\eta_{{\\rm the}} = {eta_the:.3f}±{ec_etat:.3f}')
# print(f'\\eta_{{\\rm exp}} = {eta_exp:.3f}±{ec_etaexp:.3f}')
#
# EN_eta = abs(eta_the-eta_exp)/(np.sqrt(ec_etat**2+ec_etaexp**2))
# print(EN_eta)
