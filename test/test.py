import numpy as np

# rho = 2.7e3 # kg.m-3
# a = 20e-6   # m
# S = 5e-2    # m²
# k = 1000    # N.m⁻¹
# e = 3e-3    # m
# z0 = -e/100 # m
#
# T0 = 2*np.pi*np.sqrt(rho*a*S/k*((e+z0)/(e+3*z0)))
# print(f'T_0 = {T0:.2e}')

h = 4 # m
n = 2.3
alpha = h/(2*np.pi*n)
print(f'\\alpha = \\SI{{{alpha:.2f}}}{{m.rad^{{-1}}}}')
