def eucdis(x1,y1,r1,x2,y2,r2):
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    md = max(0,d-r1-r2)
    if(d<abs(r1-r2)):
        md = abs(r1-r2)-d
    return [md,d+r1+r2]
n,q = [int(i) for i in input().split()]
a = []
d = []
for i in range(n):
    b = [float(j) for j in input().split()]
    a.append(b)
for i in range(n-1):
    for j in range(i+1,n):
        d.append(eucdis(a[i][0],a[i][1],a[i][2],a[j][0],a[j][1],a[j][2]))
l = {}
for i in range(q):
    c = 0
    m = float(input())
    if m not in l:
        for j in d:
            if(j[0]<=m and j[1]>=m):
                c+=1
        l[m] = c
    else:
        c = l[m]
    print(c)
