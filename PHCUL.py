from math import sqrt,inf
for i in range(int(input())):
    x,y = [int(j) for j in input().split()]
    n,m,k = [int(j) for j in input().split()]
    an = [int(j) for j in input().split()]
    am = [int(j) for j in input().split()]
    ak = [int(j) for j in input().split()]

    a1,a3,a5,a6 = [],[],[],[]

    for j in range(m):
        mi = inf
        for q in range(k):
            p = (ak[q+q]-am[j+j])*(ak[q+q]-am[j+j])+(ak[q+q+1]-am[j+j+1])*(ak[q+q+1]-am[j+j+1])
            mi = min(mi,p)
        a1.append(mi)

    for j in range(m):
        a1[j] = sqrt(a1[j])

    for j in range(n):
        mi = inf
        for q in range(k):
            p = (ak[q+q]-an[j+j])*(ak[q+q]-an[j+j])+(ak[q+q+1]-an[j+j+1])*(ak[q+q+1]-an[j+j+1])
            mi = min(mi,p)
        a3.append(mi)
    
    for j in range(n):
        a3[j] = sqrt(a3[j])

    for j in range(n):
        a5.append(sqrt((an[j+j]-x)*(an[j+j]-x)+(an[j+j+1]-y)*(an[j+j+1]-y)))

    for j in range(m):
        a6.append(sqrt((am[j+j]-x)*(am[j+j]-x)+(am[j+j+1]-y)*(am[j+j+1]-y)))

    mi = inf
    for j in range(n):
        for q in range(m):
            p = sqrt((an[j+j]-am[q+q])*(an[j+j]-am[q+q])+(an[j+j+1]-am[q+q+1])*(an[j+j+1]-am[q+q+1]))
            mi = min(a1[q]+a5[j]+p,a3[j]+a6[q]+p,mi)

    print(mi)

    
