from collections import Counter as co
##for i in range(int(input())):
##    n,m,k = [int(j) for j in input().split()]
##    for j in range(n):
##        p = [int(k) for k in input().split()]
##        pp = co(p)
##        if(len(pp.most_common(10000))>1 and pp.most_common(2)[0][1]==pp.most_common(2)[1][1]):
##            print(pp.most_common(10000)[1][0], end=' ')
##        else:
##            print(pp.most_common(10000)[0][0], end=' ')
##    

for i in range(int(input())):
    n,m,k = [int(j) for j in input().split()]
    a = [0 for j in range(k)]
    pp = []
    for j in range(n):
        p = [int(k) for k in input().split()]
        pp.append(p)
        q = dict(co(p))
        s = max(list(q.values()))
        qq = set()
        for k in list(q.keys()):
            if(q[k]==s):
                qq.add(k)
        for k in range(len(p)):
            if(p[k] in qq):
                a[k]+=1
    k = a.index(max(a))
    for j in range(n):
        print(pp[j][k],end=' ')
