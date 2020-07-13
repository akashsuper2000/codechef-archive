import sys
modulo = pow(10,9)+7

def postfix(a,n):
    for i in range(n-1,0,-1):
        a[i-1]+=a[i]

def modify(a,b,n):
    for i in range(1,n):
        a[i-1] = b[i-1]*a[i]

def ac(a,n):
    s = sum(a)
    b = a[:]
    s = s%modulo
    for i in range(1,min(n,8000)):
        postfix(a,8000-i+1)
        for j in range(1,8000-i):
            s+=b[j-1]*a[j]
        modify(a,b,8000)
    s = s%modulo
    return s
        

n,k = [int(i) for i in sys.stdin.readline().split()]
a = [int(i) for i in sys.stdin.readline().split()]
d = [0]*8000
for i in a:
    d[i-1]+=1
print(ac(d,k)+1)

