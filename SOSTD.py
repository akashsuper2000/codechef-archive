k = 10**9 + 7
import itertools as it
for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    s = max(a)*max(b)
    p,q = [],[]
    for j in range(1,n):
        p.extend(list(it.combinations(a,j)))
        q.extend(list(it.combinations(b,j)))
    for j in range(len(p)):
        s+=max(p[j])*max(q[j])
    print(s%k)
