from itertools import accumulate as ac
def fac(x):
    a = []
    for i in range(1, x + 1):
        if x % i == 0 and i<27:
            a.append(i)
    return a


for i in range(int(input())):
    s = input()
    l = len(s)
    m = 10**9
    p = [0 for j in range(26)]
    a = fac(l)
    for j in s:
        p[ord(j)-65]+=1
    p.sort(reverse = True)
    q = list(ac(p))
    for j in a:
        n = l/j
        f = 0
        c = 0
        for k in range(j):
            if(p[0]>n):
                f = 1
                c+=max(0,p[k]-n)
            else:
                c+=n-p[k]
        if(f==1):
            c+=q[-1]-q[j-1]
        m = min(c,m)
    print(int(m))
