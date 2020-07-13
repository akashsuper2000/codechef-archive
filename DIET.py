for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    f = -1
    c = 0
    a = [int(j) for j in input().split()]
    for i in range(n):
        if(a[i]+c<k):
            f = i
            break
        c = a[i]+c-k
    if(f==-1):
        print('YES')
    else:
        print('NO',f+1)
