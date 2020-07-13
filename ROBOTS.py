for i in range(int(input())):
    a = []
    n,q = [int(j) for j in input().split()]
    s = input()
    m,n,d = 0,0,0
    abc = [[1,0],[0.5,1],[-0.5,1],[-1,0],[-0.5,-1],[0.5,-1]]
    for j in s:
        m+= abc[(d+int(j))%6][0]
        n+= abc[(d+int(j))%6][1]
        d = (d+int(j))%6
        a.append([m,n,d])
    for j in range(q):
        l,r = [int(k) for k in input().split()]
        a1,a2 = a[r-1][0]-a[l-1][0],a[r-1][1]-a[l-1][1]
        print(a1*1.000000,a2*0.866025)
