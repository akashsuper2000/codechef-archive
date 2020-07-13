def pf(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for i in range(int(input())):
    n = int(input())
    t = 0
    a = [int(j) for j in input().split()]
    c = []
    for j in range(n):
        c.append(sum(pf(a[j])))
    for j in range(n):
        for k in range(n):
            if a[k]%a[j]==0 and c[k]%c[j]==0 and k!=j:
                t = t+1
    print(int(t))
