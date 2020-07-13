import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return int(numer / denom)

for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    a.sort()
    b = a[:k]
    n,r = a.count(b[-1]),b.count(b[-1])
    print(ncr(n,r))
    
