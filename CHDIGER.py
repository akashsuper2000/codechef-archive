for i in range(int(input())):
    n,d = [j for j in input().split()]
    d = int(d)
    n = [int(j) for j in str(n)]
    ind = -1
    c = len(n)
    m = 10
    while(ind<len(n)-1):
        m = min(n[ind+1:])
        p = ind+1
        ind = n[ind+1:].index(m)
        ind+=p
        if(m<d):
            print(m,end = '')
            c-=1
    if(c>0):
        print(str(d)*c)
    else:
        print()
        
