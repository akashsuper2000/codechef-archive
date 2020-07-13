def sod(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

from math import gcd

k = 10**9+7
for i in range(int(input())):
    l,r = [int(j) for j in input().split()]
    a = [j for j in range(l,r+1)]
    a = [sod(j) for j in a]
    c = 0
    for j in range(r-l+1):
        for k in range(j+1,r-l+1):
            if gcd(a[j],a[k])==1:
                c = c+1
    print(c%k)
