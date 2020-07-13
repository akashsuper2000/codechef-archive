for i in range(int(input())):
    n,x,s = [int(j) for j in input().split()]
    for j in range(s):
        a = [int(k) for k in input().split()]
        if(x==a[0]):
            x = a[1]
        elif(x==a[1]):
            x = a[0]
    print(x)
