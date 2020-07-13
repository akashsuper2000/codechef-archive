for i in range(int(input())):
    a = [int(j) for j in input().split()]
    t=0
    for j in range(3):
        for k in range(a[j]+1):
            p = k+a[(j+1)%3]
            q = a[j]-k+a[(j+2)%3]
            r = k+a[(j+2)%3]
            s = a[j]-k+a[(j+1)%3]
            if (p==a[3] and q==a[4]) or (r==a[3] and s==a[4]):
                t=1
    if t==1:
        print("YES")
    else:
        print("NO")
