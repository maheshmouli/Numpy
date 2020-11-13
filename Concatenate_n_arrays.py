import numpy as np

n, m, p = map(int, input().split())
arrN = np.array([input().split() for i in range(n)], int)
arrM = np.array([input().split() for j in range(m)], int)
print(np.concatenate((arrN, arrM)))
    