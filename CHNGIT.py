for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    d = {}
    for j in a:
        if(j in d):
            d[j]+=1
        else:
            d[j] = 1
    print(n-max(list(d.values())))
