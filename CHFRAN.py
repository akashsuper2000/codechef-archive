for i in range(int(input())):
    n = int(input())
    a = []
    for j in range(n):
        l,r = [int(k) for k in input().split()]
        a.append((l,0))
        a.append((r,1))
    a.sort()
    c = 0
    f = 0
    m = 1e5
    for j in a:
        if(j[1]):
            f=1
            c-=1
        else:
            if(f==1):
                m=min(m,c)
            c+=1
    if(m==int(1e5)):
        print(-1)
    else:
        print(m)
