from math import ceil
def nos(ns,noe):
    k = ceil(ns/noe)
    n = (ns/k)
    m = int(n)
    if(n>m):
        m+=1
    return m

for i in range(int(input())):
    m,noe,nof = [int(j) for j in input().split()]
    c=0
    if(nof>noe):
        print(0)
    else:
        for j in range(1,m+1):
            if(nos(j,noe)==nof):
                c+=1
        print(c)
    
