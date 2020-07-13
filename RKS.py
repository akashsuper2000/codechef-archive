for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    m,s = set(),set()
    for j in range(k):
        a,b = [int(p) for p in input().split()]
        m.add(a-1)
        s.add(b-1)
    c = 0
    l = []
    for j in range(n):
        if(j not in m):
            for k in range(n):
                if(k not in s):
                    c+=1
                    l.append(j+1)
                    l.append(k+1)
                    m.add(j)
                    s.add(k)
                    break
    print(c,*l)
