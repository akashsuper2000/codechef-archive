def m(a,n,b,c,d):
    if n<0:
        return(abs(b-c))
    k = str(n)+'|'+str(b)
    try:
        return d[k]
    except:
        inc = m(a,n-1,b+a[n],c,d)
        exc = m(a,n-1,b,c+a[n],d)
        d[k] = min(inc,exc)
        return d[k]
    

for i in range(int(input())):
    d = {}
    n = int(input())
    a = [int(j) for j in input().split()]
    if len(set(a))-n!=0:
        print(0)
    else:
        print(m(a,n-1,0,0,d))
