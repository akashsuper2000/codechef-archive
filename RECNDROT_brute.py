for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    p = list(set(a))
    c = 0
    f = 0
    while(f<len(p)-1):
        c+=1
        for j in range(n):
            if(f==len(p)-1):
                break
            if(p[f+1]==a[j]):
                f+=1
    print(c)
