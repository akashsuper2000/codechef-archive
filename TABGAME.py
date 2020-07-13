def res(m,n,d):
    if (m,n) in d:
        return d[(m,n)]
    if (m-1,n) not in d:
        d[(m-1,n)] = res(m-1,n,d)
    if (m,n-1) not in d:
        d[(m,n-1)] = res(m,n-1,d)
    d[(m,n)] = int(not(d[(m-1,n)] & d[(m,n-1)]))
    return d[(m,n)]


for i in range(int(input())):
    s = ''
    d = {}
    m = input()
    n = input()
    for j in range(len(n)):
        d[(j+1,0)] = int(n[j])
    for j in range(len(m)):
        d[(0,j+1)] = int(m[j])
    for j in range(int(input())):
        p,q = [int(k) for k in input().split()]
        s = s+str(res(p,q,d))
    print(s)
