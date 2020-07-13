for i in range(int(input())):
    a = [[0,0] for j in range(4)]
    s = []
    for j in range(12):
        k = [p for p in input().split()]
        k[1],k[3] = int(k[1]),int(k[3])
        if(k[0] not in s):
            s.append(k[0])
        if(k[4] not in s):
            s.append(k[4])
        m,n = s.index(k[0]),s.index(k[4])
        if(k[1]>k[3]):
            a[m][0]+=3
            a[m][1]+=k[1]-k[3]
            a[n][1]+=k[3]-k[1]
        elif(k[1]<k[3]):
            a[n][0]+=3
            a[n][1]+=k[3]-k[1]
            a[m][1]+=k[1]-k[3]
        else:
            a[m][0]+=1
            a[n][0]+=1
    c = list(zip(a,s))
    c.sort(reverse=True)
    print(c[0][1],c[1][1])
