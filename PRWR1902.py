d = {1:'ON',0:'OFF'}
for i in range(int(input())):
    f,s1,s2 = [int(j) for j in input().split()]
    for j in range(int(input())):
        a,b = [int(k) for k in input().split()]
        p = abs(s1-a)+abs(s2-b)
        if(p%2==0):
            print(d[f])
        else:
            print(d[abs(f-1)])
