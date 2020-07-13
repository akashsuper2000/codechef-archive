n,m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a = [[i,j] for i,j in enumerate(a)]
b = [[i,j] for i,j in enumerate(b)]
a.sort(key = lambda i: i[1])
b.sort(key = lambda i: i[1])
p = set()
c = 0
if(n>m):
    for i in range(n):
        if(c>=n+m-1):
            break
        if(b[0][1]+a[i][1] not in p):
            p.add(b[0][1]+a[i][1])
            print(a[i][0],b[0][0])
            c+=1
        if(b[-1][1]+a[i][1] not in p):
            p.add(b[-1][1]+a[i][1])
            print(a[i][0],b[-1][0])
            c+=1
else:
    for i in range(m):
        if(c>n+m-1):
            break
        if(b[i][1]+a[0][1] not in p):
            p.add(b[i][1]+a[0][1])
            print(a[0][0],b[i][0])
            c+=1
        if(b[i][1]+a[-1][1] not in p):
            p.add(b[i][1]+a[-1][1])
            print(a[-1][0],b[i][0])
            c+=1
        
