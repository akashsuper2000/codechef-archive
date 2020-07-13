for i in range(int(input())):
    n,q = [int(j) for j in input().split()]
    c = 0
    p = 0
    for j in range(q):
        a,b = [int(k) for k in input().split()]
        c+=abs(p-a)
        p = a
        c+=abs(p-b)
        p = b
    print(c)
