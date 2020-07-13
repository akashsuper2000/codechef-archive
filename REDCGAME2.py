for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    
    a = [int(j) for j in input().split()]
    a.sort()
    f = sum(a)
    dif = 0
    sl = 0
    l = 0
    for j in a:
        if j>k:
            dif += j-k
            sl = l
            l = j-k
                
    dif-=l
    if dif>=2*sl:
        print(f-dif-2*(dif%2))
    else:
        print(f-(2*sl))
