for i in range(int(input())):
    n,m,q = [int(j) for j in input().split()]
    am = [int(j) for j in input().split()]
    aq = [int(j) for j in input().split()]
    s = [0 for j in range(n)]
    d = {}
    for j in am:
        d[j-1] = 1
    for j in aq:
        for k in range(j-1, n, j):
            if(k not in d):
                s[k]+=1
    print('Case #'+str(i+1)+': '+str(sum(s)))
