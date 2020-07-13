for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    a.reverse()
    b = [0]
    c = 0
    for j in range(1,n):
        if(a[j]<a[j-1]):
            c = j
            b.append(c)
        else:
            b.append(c)
    b.reverse()
    print(*b)
