def swap(p,j,k,n):
    a = p[j]
    b = []
    for m in range(n):
        b.append(p[m][k])
    for m in range(n):
        p[m][k] = a[m]
    p[j] = b

for i in range(int(input())):
    n = int(input())
    p,q = [],[]
    for j in range(n):
        p.append([int(k) for k in input().split()])
    for j in range(n):
        q.append([int(k) for k in input().split()])
    f = 0
    for j in range(n):
        for k in range(n):
            if(p[j][k]!=q[j][k] and p[j][k]==q[k][j]):
                swap(p,j,k,n)
            elif(p[j][k]==q[j][k]):
                continue
            else:
                f = 1
    for j in range(n):
        for k in range(n):
            if(p[j][k]!=q[j][k]):
                f = 1
                break
        if(f==1):
            break
    
    if(f==1):
        print('No')
    else:
        print('Yes')
