for i in range(int(input())):
    d = {}
    for j in range(int(input())):
        n,p = [k for k in input().split()]
        p = int(p)
        if((n,p) in d):
            d[(n,p)]+=1
        else:
            d[(n,p)] = 1
    s = 0
    for j in list(d.keys()):
        if((j[0],0) in d and (j[0],1) in d):
            a = d[(j[0],0)]
            b = d[(j[0],1)]
            if(a>b):
                s+=d[(j[0],0)]/2
            else:
                s+=d[(j[0],1)]/2
        else:
            s+=d[j]
    
    print(int(s))
