m = 10**9+7
for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    if(k<=n):
        print((k-1)%m)
    else:
        k-=1
        n-=1
        if(k%n==0):
            nn=k//n
        else:
            nn=k//n+1
        n = -n
        c = ((nn%m)*((2*((k%m)%m))+((nn-1)%m)*((n%m)%m)))%m
        c*=500000004
        c+=m
        c%=m
        print(c%m)
