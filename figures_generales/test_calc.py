import numpy as np

vals = np.array([11.9, 12.5, 13.1, 12.4, 12.9, 12.6, 12.8, 12.6])
mean = np.mean(vals)
ecarttype = np.std(vals, ddof=1)
incertype = ecarttype/np.sqrt(len(vals))
print(f'D = {mean:.2f} +- {incertype:.2f}')
