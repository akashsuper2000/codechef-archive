from sys import stdin, stdout
def main():
    n,m = [int(x) for x in stdin.readline().split()]
    a = [int(x) for x in stdin.readline().split()]
    b = [int(x) for x in stdin.readline().split()]
    #n,m = [int(i) for i in input().split()]
    #a = [int(i) for i in input().split()]
    #b = [int(i) for i in input().split()]
    c = [a[i]*b[i] for i in range(n)]
    l = 0
    r = max(c)+1
    ans=r
    while(l<r):
        h = int((l+r)/2)
        v = 0
        for i in range(n):
            if(c[i]>h):
                p = (c[i]-h)/b[i]
                if(p-int(p)>0):
                    p = int(p)+1
                v+=p
        if(v<=m):
            ans=min(ans,h)
            r = h
        else:
            l = h+1
    #h = int((l+r)/2)
    print(ans)
if __name__=='__main__':
    main()
