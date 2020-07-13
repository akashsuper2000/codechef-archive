from functools import reduce
def ands(p,q):
    return p&q
def check(n):
    if(n==0 or n==1):
        return True
    
    return (n**0.5).is_integer()

for i in range(int(input())):
    n,q = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    for j in range(q):
        c = 0
        l,r = [int(k) for k in input().split()]
        b = a[l-1:r]
        for k in range(len(b)):
            for l in range(k+1,len(b)+1):
                m = b[k:l]
                if(len(m)>0):
                    if(check(reduce(ands,m))):
                        c = c+1
        print(c)
