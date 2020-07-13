for i in range(int(input())):
    D = int(input())
    m = [0 for k in range(31)]
    c = 0
    e = 0
    for k in range(D):
        a,b = [int(j) for j in input().split()]
        
        for j in range(e,a-1):
            m[j] = c
        c+=b
        m[a-1] = c
        e = a
        
    q = int(input())
    for k in range(q):
        a,b = [int(j) for j in input().split()]
        if(m[a-1]<b):
            print('Go Sleep')
        else:
            print('Go Camp')