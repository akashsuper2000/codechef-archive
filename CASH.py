for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    b = [j%k for j in a]
    c = [k-j for j in b]
    ss = sum(c)
    s = sum(b)
    ps = 0
    pss = 0
    m = 1e9
    for j in range(n):
        ps+=b[j]
        pss+=c[j]
        if(ps>=ss-pss):
            m = min(m,ps-ss+pss)
    print(m)
