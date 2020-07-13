import numpy as np
n,m,q = [int(i) for i in input().split()]
for i in range(q):
    a = input()
p = np.random.randint(1,50)
print(n,m,p)
for i in range(p):
    print(np.random.randint(1,3),np.random.randint(1,min(n,m)))
