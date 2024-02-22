import numpy as np

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
#
# v1 = np.sqrt(G*M/r1)
# ve1 = np.sqrt(2*G*M*r2/(r1*(r1+r2)))
# Dvp = ve1-v1
# print(f'v_1 = {v1:.1f}, v_e1 = {ve1:.1f}, D v_P = {Dvp:.1f}')
# # Wpp = 17e9 # J
# # m = 2*Wpp/(ve1**2-v1**2)
# m = 1000  # kg
# print(f'm = {m:.2e} kg')
# Wp = G*m*M*(r2-r1)/(2*r1*(r1+r2))
# print(f'Wp = {Wp/1e9:.0f} GJ')
# Wa = (G*M*m*(r2-r1))/(2*r2*(r1+r2))
# print(f'Wa = {Wa/1e9:.1f} GJ')

# M7
# Tsid = 23*3600+56*60+4
# w_sid = 2*np.pi/(Tsid)
# print(f'w_sid = {w_sid:.2e} rad.s^-1')

# DS06
B = 1.0 # T
eSm = 2e11 # SI
a = 1.0e-3 # m
v = 2.0e8  # m.s^-1
Dt = a*B*eSm/v
print(f'Delta\\th = {Dt} rad = {Dt*180/np.pi}°')
