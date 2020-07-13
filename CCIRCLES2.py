from math import ceil
n,q = [int(i) for i in input().split()]
a = []
d = [[0]*2 for i in range(10**6)]
for i in range(n):
    b = [float(j) for j in input().split()]
    a.append(b)
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1,r1,x2,y2,r2 = a[i][0],a[i][1],a[i][2],a[j][0],a[j][1],a[j][2]
        di = ((x2-x1)**2+(y2-y1)**2)**0.5
        md = max(0,di-r1-r2)
        if(di<abs(r1-r2)):
            md = abs(r1-r2)-di
        d[ceil(md)][0]+=1
        d[int(di+r1+r2)+1][1]-=1
m = [0]*10**6
c = 0
for i in range(10**6):
    c+=d[i][0]+d[i][1]
    m[i] = c
for i in range(q):
    print(m[int(input())])
