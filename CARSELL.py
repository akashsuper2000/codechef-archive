mod = int(1e9)+7
for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    a.sort(reverse=True)
    c = 0
    for i in range(n):
        c = (c+max(a[i]-i,0))%mod
    print(c)
        
