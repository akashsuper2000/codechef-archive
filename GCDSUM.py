from math import gcd
from functools import reduce
a = [int(i) for i in input().split()]
n,m = a[0],a[1]
a=[]
for i in range(n):
    b = [int(j) for j in input().split()]
    a.append(b)
