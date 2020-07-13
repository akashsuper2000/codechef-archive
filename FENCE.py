for i in range(int(input())):
    n,m,k = [int(j) for j in input().split()]
    ans = int(k*4)
    d = set()
    for j in range(k):
        r,c = [int(p) for p in input().split()]
        if((r-1,c) in d):
            ans-=2
        if((r,c-1) in d):
            ans-=2
        if((r+1,c) in d):
            ans-=2
        if((r,c+1) in d):
            ans-=2
        d.add((r,c))
    print(ans)
