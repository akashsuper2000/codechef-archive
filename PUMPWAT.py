def fun(a):
    if(len(a)==0):
        return 0
    if(len(a)==1 or len(a)==2):
        return 1
    p = max(a)
    if(a.index(p)==0 or a.index(p)==len(a)-1):
        return 1
    return 1+min(fun(a[:a.index(p)]),fun(a[a.index(p)+1:]))

for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    print(fun(a))
