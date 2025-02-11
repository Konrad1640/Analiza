import numpy as np

# Układ równań:
# 2x + 3y = 8
# 5x - 2y = 4

A = np.array([[2,3], [5, -2]]) # Macierz współczynników
B = np.array([8, 4]) # Macierz wyników

X = np.linalg.solve(A, B)
print("Rozwiązanie: x =", X[0], ", y =", X[1])