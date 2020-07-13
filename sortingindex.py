c = 0
def fun(l,r,i):
    if(l[i]==-1):
        l[i] = r[i]
        return
    fun(l,r,l[i])
    fun(l,r,r[i])
    if(l[l[i]]==-1 or r[r[i]]==-1):
        l[i],r[i] = -1,-1
        return
    if(l[l[i]]>r[r[i]]):
        global c
        c+=1
        l[i],r[i] = l[r[i]],r[l[i]]
    elif(r[l[i]]<l[r[i]]):
        l[i],r[i] = l[l[i]],r[r[i]]
    else:
        l[i],r[i] = -1,-1

for i in range(int(input())):
    n = int(input())
    c = 0
    l,r = [0 for j in range(n)],[0 for j in range(n)]
    for j in range(n):
        l[j],r[j] = [int(k) for k in input().split()]
        r[j]-=1
        if(l[j]!=-1):
            l[j]-=1
    fun(l,r,0)
    if(l[0]==-1):
        print(-1)
    else:
        print(c)
