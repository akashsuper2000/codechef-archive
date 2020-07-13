from math import ceil
for i in range(int(input())):
    n = int(input())
    c = [int(j) for j in input().split()]
    x = int(input())
    r = n
    p,q = 0,n-1
    while(r>0):
        if(ceil(c[p]/x)==c[q]):
            if(r>1):
                p+=1
                q-=1
                r-=2
            elif(p>=q-n+1):
                p+=1
                r-=1
            else:
                q-=1
                r-=1
        elif(ceil(c[p]/x)>c[q]):
            c[p]-=c[q]*x
            q-=1
            r-=1
        else:
            c[q]-=ceil(c[p]/x)
            p+=1
            r-=1
    print(p,n-p)
                    
