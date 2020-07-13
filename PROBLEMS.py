a = input().split()
p,s = int(a[0]),int(a[1])
n = []
for i in range(p):
    t=0
    sc = [int(j) for j in input().split()]
    ns = [int(j) for j in input().split()]
    sc,ns = [x for x,y in sorted(zip(sc,ns))],[y for x,y in sorted(zip(sc,ns))]
    for j in range(s-1):
        for k in range(j+1,s):
            if ns[j]>ns[k]:
               t = t+1
    n.append([t,i+1])
n.sort()
print('\n'.join([str(i[1]) for i in n]))
