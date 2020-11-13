import numpy as np
np.set_printoptions(legacy = '1.13') #used to print the output with correct 
                                     #spaces(Can ignore this)

n,m = map(int, input().split())
print(np.eye(n,m, k= 0))