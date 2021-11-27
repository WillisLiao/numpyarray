import numpy as np
A = np.array([[-1, 2, 3],
              [4, 0, 5],])
B = np.array([[5, -1],
              [-4, 0],
              [2, 3]])

print(A.dot(B))
print(B.dot(A))