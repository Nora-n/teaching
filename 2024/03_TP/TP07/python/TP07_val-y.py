a = 0  # s
b = 10  # s
n = 100  # points de calculs
y0 = 0  # condition initiale
list_y = euler(f, a, b, y0, n)  # list_y est un vecteur des valeurs de y
