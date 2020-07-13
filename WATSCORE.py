for i in range(int(input())):
    n = int(input())
    a = [0 for j in range(8)]
    for j in range(n):
        p,q = [int(k) for k in input().split()]
        if(p<9):
            if(a[p-1]<q):
                a[p-1] = q
    print(sum(a))
