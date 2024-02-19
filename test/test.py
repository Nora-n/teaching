import numpy as np

m = 10.4e-3    # kg
tau = 73.5e-3  # s
R = 1.0e-2     # m
eta = m/(6*np.pi*tau*R)
print(f'\\eta = {eta}')
