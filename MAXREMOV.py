for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    c1 = [0 for j in range(100000)]
    c2 = [0 for j in range(100000)]
    c = [0 for j in range(100000)]
    for j in range(n):
        l,r = [int(j) for j in input().split()]
        c1[l-1]+=1
        c2[r-1]+=1
    p = 0
    for j in range(100000):
        p+=c1[j]
        c[j] = p
        p-=c2[j]
