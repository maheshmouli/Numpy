import numpy as np

n,m = input().split()
a = []
for i in range(int(n)):
	array = input().split()
	a.append(array)
lis1 = np.array(a, int)
print(np.transpose(lis1))
print(lis1.flatten())