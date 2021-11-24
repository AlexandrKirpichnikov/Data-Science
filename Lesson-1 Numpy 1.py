import numpy as np

a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])
print(a)

mean_a = a.mean(axis=0)
print(mean_a)