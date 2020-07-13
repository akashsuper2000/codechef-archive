for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [[0]*2 for j in range(10**9)]
    for p in range(n):
        l,r = [int(j) for j in input().split()]
        a[l][0]+=1
        a[r][1]-=1
    b = [0]*10**9
    c = 0
    for j in range(len(a)):
        c+=a[j][0]
        b[j] = c
        c+=a[j][1]
        if(b[j]>k):
            b[j] = k
    c = 0
    m = 0
    for j in range(len(a)):
        if(b[j]!=k):
            if(c>m):
                m = c
            c = 0
        else:
            c+=1
    print(m)
