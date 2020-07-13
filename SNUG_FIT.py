for i in range(int(input())):
    n = int(input())
    a = sorted([int(j) for j in input().split()])
    b = sorted([int(j) for j in input().split()])
    print(sum([min(a[j],b[j]) for j in range(n)]))
    
