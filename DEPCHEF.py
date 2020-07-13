for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    d = [int(j) for j in input().split()]
    m = -1
    if(a[-1]+a[1]<d[0]):
        m = max(m,d[0])
    if(a[-2]+a[0]<d[-1]):
        m = max(m,d[n-1])
    for j in range(1,n-1):
        if(a[j-1]+a[j+1]<d[j]):
            m = max(m,d[j])
    print(m)
