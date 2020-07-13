from math import gcd
k = 10**9+7
for i in range(int(input())):
    a = [int(i) for i in input().split()]
    if a[0]==a[1]:
        g = a[0]**a[2]+a[1]**a[2]
    else:
        g = gcd(a[0],a[1])
        a[0],a[1] = a[0]/g,a[1]/g 
        if a[0]%2!=0 and a[1]%2!=0:
            g = g*2
    print(g)
