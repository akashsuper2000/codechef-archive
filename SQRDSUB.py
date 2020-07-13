def fun(n):
    p = []
    for i in range(len(n)):
        if(n[i]==0):
            p.append(0)
        elif(n[i]%2==0 and n[i]%4!=0):
            p.append(1)
        elif(n[i]%4==0):
            p.append(0)
        else:
            p.append(-1)
    return p

for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    c = (n*(n+1))//2
    p = fun(a)
    f = 0
    s = [0,0]
    for j in range(n):
        if(f==0):
            if(p[j]==0):
                s[0] = 0
            elif(p[j]==1):
                f = 1
            else:
                s[0]+=1
        elif(f==1):
            if(p[j]==0):
                c = c-((s[0]+1)*(s[1]+1))
                f = 0
                s[0] = 0
                s[1] = 0
            elif(p[j]==1):
                c = c-((s[0]+1)*(s[1]+1))
                s[0] = s[1]
                s[1] = 0
            else:
                s[1]+=1
    if(f==1):
        c = c-((s[0]+1)*(s[1]+1))
    print(c)
    
