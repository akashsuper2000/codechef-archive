for i in range(int(input())):
    a = [int(j) for j in input().split()]
    n,r = a[0],a[1]
    a = [int(j) for j in input().split()]
    x = len(a)
    y = len([j for j in a if j<=r])
    print(x,y,y)
