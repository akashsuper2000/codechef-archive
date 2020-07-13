for i in range(int(input())):
    n,p = [int(j) for j in input().split()]
    print(min(n-p,p-1))
