from math import gcd
for i in range(int(input())):
    n,a,b,k = [int(j) for j in input().split()]
    p = int(n/a)+int(n/b)-int((n*gcd(a,b))/(a*b))
    if(a>b):
        if(a%b==0):
            p-=int(n/a)
    elif(a==b):
        p=0
    else:
        if(b%a==0):
            p-=int(n/b)
    if(p>=k):
        print('Win')
    else:
        print('Lose')
