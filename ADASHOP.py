for i in range(int(input())):
    n,m,r,c,k = [int(j) for j in input().split()]
    b=[r,c]
    m=0
    while(k>0):
        if(j+1 in b) and (l+1 in b):
            pass
        elif(j+1 in b) or (l+1 in b):
            b.append(j+1)
            b.append(l+1)
            m+=1
                    
        k-=1
    print(m+1)
