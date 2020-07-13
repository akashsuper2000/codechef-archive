for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    s = [int(j) for j in input().split()]
    s.sort(reverse=True)
    p = s[k-1]
    print(s.count(p)+s.index(p))
