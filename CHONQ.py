def fun(a):
    c = 0
    for i in range(len(a)):
        c+=int(a[i]/(i+1))
    return c

for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]+[0]
    for j in range(n+1):
        if(fun(a[j:])<=k):
            print(j+1)
            break
        
