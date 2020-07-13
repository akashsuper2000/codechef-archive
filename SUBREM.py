def rem(d,n):
    for i in d[n]:
        d[i].remove(n)
        rem(d,i)

def fun(d,v,k,n):
    if(n in k):
        return k[n]
    s = v[n-1]
    for i in d[n]:
        s+=fun(d,v,k,i)
    k[n] = s
    return s

def func(d,v,k,x,n):
    m = 0
    for i in d[n]:
        m+=func(d,v,k,x,i)
    m = max(-k[n]-x,m)
    return m


for i in range(int(input())):
    n,x = [int(j) for j in input().split()]
    v = [int(j) for j in input().split()]
    d = {j+1:set() for j in range(n)}
    for j in range(n-1):
        a,b = [int(p) for p in input().split()]
        d[a].add(b)
        d[b].add(a)
    rem(d,1)
    k = {}
    ans = fun(d,v,k,1)
    ans+=func(d,v,k,x,1)
    print(ans)
