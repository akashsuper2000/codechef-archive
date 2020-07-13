def res(m,n,p,q):
    if (p,q) in d:
        return d[(p,q)]
    a1,a2 = 1,1
    if(p==1):
        a2 = int(n[q-1])
    elif(p%2!=0 and int(n[q-1])==0):
        a2 = res(m,n,p-1,q)
    elif(p%2==0 and int(n[q-1])==1):
        a2 = res(m,n,p-1,q)
        
    if(q==1):
        a1 = int(m[p-1])
    elif(q%2!=0 and int(m[p-1])==0):
        a1 = res(m,n,p,q-1)
    elif(q%2==0 and int(m[p-1])==1):
        a1 = res(m,n,p,q-1)

    d[(p,q)] = (int(not(a1&a2)))
    return d[(p,q)]


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
        s = s+str(res(m,n,q,p))
    print(s)
