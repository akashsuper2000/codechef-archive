for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    ii = -1+a[0]
    b = [ii]
    psum = ii+a[0]
    b.append(a[0])
    f = 1
    c = ii
    if(not pow(ii,0.5).is_integer()):
        f = 0
    for j in range(1,n):
        print(psum)
        if(not pow(psum,0.5).is_integer() or f==0):
            f = 0
            break
        ii+=a[j]
        
        psum+=a[j]-c
        print(psum)
        b.append(psum)
        b.append(a[j])
        if(not pow(psum,0.5).is_integer() or f==0):
            f = 0
            break
        c = ii-a[j]
        print(*b)

    if(f==0):
        print(-1)
    else:
        print(*b)
    
