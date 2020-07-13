for i in range(int(input())):
    r,c,k = [int(j) for j in input().split()]
    r-=1
    c-=1
    p = 0
    for j in range(8):
        for m in range(8):
            if(abs(j-r)<=k and abs(m-c)<=k):
                p+=1
    print(p)
