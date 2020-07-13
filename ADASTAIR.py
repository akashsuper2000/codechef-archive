for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    h = [int(j) for j in input().split()]
    c = 0
    if(h[0]-0)>k:
        c=(h[0]-0)//k
        if(h[0]-0)%k==0:
                c-=1
    for j in range(n-1):
        if(h[j+1]-h[j])>k:
            c+=(h[j+1]-h[j])//k
            if(h[j+1]-h[j])%k==0:
                c-=1
    print(c)
