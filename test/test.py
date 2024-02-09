import numpy as np

m = 10.4e-3
tau = 73.5e-3
R = 1.0e-2
eta = m/(6*np.pi*tau*R)
print(f'\\eta = {eta}')
