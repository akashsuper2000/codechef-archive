from math import gcd
from functools import reduce

def fun(a):
    return reduce(gcd,a)

for i in range(int(input())):
    n = int(input())
    a = list(set([int(j) for j in input().split()]))
    if(len(a)==1):
        print(a[0]+a[0])
    else:
        b = max(a)
        a.remove(b)
        m = b+fun(a)
        c = max(a)
        a.remove(c)
        a.append(b)
        print(max(m,c+fun(a)))
    
