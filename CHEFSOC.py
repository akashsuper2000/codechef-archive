def fun(a):
    if(len(a)==0):
        return 0
    if(len(a)==1):
        return 1
    if(len(a)==2):
        return 2
    return 1+a[0]*(fun(a[1:]))

for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    print(int(fun(a)))
