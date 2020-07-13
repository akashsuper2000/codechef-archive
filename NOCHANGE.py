from math import ceil
for i in range(int(input())):
    n,p = [int(j) for j in input().split()]
    f = 0
    a = [int(j) for j in input().split()]
    ans = [0 for j in range(n)]
    for j in range(n):
        if(p%a[j]!=0):
            f = 1
            break
    if(f==1):
        ans[j] = ceil(p/a[j])
    else:
        for j in range(1,n):
            if(a[j]%a[j-1]!=0):
                f = 1
                break
        if(f==1):
            ans[j-1],ans[j] = ceil((p-a[j])/a[j-1]),1
    if(f==1):
        print('YES',*ans)
    else:
        print('NO')
    
