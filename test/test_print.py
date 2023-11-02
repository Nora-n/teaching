import numpy as np

d = 5.5e-3
print(f'd = {d}')
print(f'd = {d:.2f}')
print(f'd = {d:.2e}')

print(np.linspace(0, 1, 3))
L = []
for i in range(3):
    L.append(3*i)
print(L)
L2 = [3*i for i in range(3)]
print(L2)
print(np.array(L)-np.array(L2))
