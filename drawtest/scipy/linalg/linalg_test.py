from scipy import linalg
import numpy as np
arr = np.array([[1, 2],
                [3, 4]])
out = linalg.det(arr)
print out
out = linalg.inv(arr)
print out


