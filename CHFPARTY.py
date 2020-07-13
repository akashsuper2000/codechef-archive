for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    a.sort()
    p = 0
    for j in range(n):
        if(p>=a[j]):
            p+=1
    print(p)
