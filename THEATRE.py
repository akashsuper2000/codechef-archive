from itertools import permutations
res = 0
for i in range(int(input())):
    n = int(input())
    d = {12:{'A':0,'B':0,'C':0,'D':0},3:{'A':0,'B':0,'C':0,'D':0},6:{'A':0,'B':0,'C':0,'D':0},9:{'A':0,'B':0,'C':0,'D':0}}
    for j in range(n):
        a,b = [k for k in input().split()]
        d[int(b)][a]+=1
    p = list(permutations(['A','B','C','D']))
    m = -400
    for j in p:
        q = 0
        c = [d[12][j[0]],d[3][j[1]],d[6][j[2]],d[9][j[3]]]
        c.sort()
        if(c[0]==0):
            q-=100
        else:
            q+=c[0]*25
        if(c[1]==0):
            q-=100
        else:
            q+=c[1]*50
        if(c[2]==0):
            q-=100
        else:
            q+=c[2]*75
        if(c[3]==0):
            q-=100
        else:
            q+=c[3]*100
        m = max(m,q)
    print(m)
    res+=m
print(res)
