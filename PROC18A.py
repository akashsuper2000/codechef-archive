for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    c = []
    for j in range(n-k+1):
        c.append(sum(a[j:j+k]))
    print(max(c))
        
        
