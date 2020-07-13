for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    c = 0
    o = [j for j in a if j%2!=0]
    lo = len(o)
    e = [j for j in a if j%2==0]
    le = len(e)
    if(lo!=0):
        for j in range(lo-1):
            for k in range(j+1,lo):
                p = o[j]^o[k]
                if(p%2==0 and p!=0 and p!=2):
                    c = c+1
    if(le!=0):
        for j in range(le-1):
            for k in range(j+1,le):
                p = e[j]^e[k]
                if(p%2==0 and p!=0 and p!=2):
                    c = c+1
    print(c)
                
