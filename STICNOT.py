for i in range(int(input())):
    n,p = int(input()),[]
    for j in range(n-1):
        p.append([int(j) for j in input().split()][2])
    q = sorted([int(j) for j in input().split()])
    p.sort()
    c,j,k = n,0,0
    while(k<n):
        if(q[k]>=p[0]):
            k,c = k+1,c-1
            break
        k+=1
    while(k<n and j<n-2):
        if(q[k]>=p[j] and q[k]>=p[j+1]):
            j,k,c=j+1,k+1,c-1
        else:
            k+=1
    print(c-int(k!=n and q[-1]>=p[-1]))
