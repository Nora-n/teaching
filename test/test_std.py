import numpy as np

vals = np.array([11.9, 12.5, 13.1, 12.4, 12.9, 12.8, 12.6])
mean = np.mean(vals)
incert = np.std(vals, ddof=1)
print(fr'D = {mean:.2f} $\pm$ {incert:.2f}')
