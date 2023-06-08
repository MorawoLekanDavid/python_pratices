import numpy as np

a = np.array([[1, 0, 3], [4, 5, 2], [7, 8, 5]])
b = np.array([10, 12, 14])
sol = np.linalg.solve(a, b)
#print(sol)

c = np.array([[1,2,3],[4,5,6],[7,8,9]])
try:
    ans = c.T @ c
except np.linalg.LinAlgError:
    print("Matrix is invertible")
else:
    print(ans)