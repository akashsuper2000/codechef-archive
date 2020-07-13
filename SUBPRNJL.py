from math import ceil
def fun(a,k):
    n = len(a)
    if(n==0):
        return False
    t = ceil(k/n)
    p = a[ceil(k/t)-1]
    if(a.count(p) in a):
        return True
    return False

for i in range(int(input())):
    n,tk = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    c = 0
    for j in range(n):
        for k in range(j+1,n+1):
            if(fun(sorted(a[j:k]),tk)):
                c+=1
    print(c)
