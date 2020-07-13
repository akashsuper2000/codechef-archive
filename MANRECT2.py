import sys
from math import ceil
for i in range(int(input())):
    print('Q',0,0)
    sys.stdout.flush()
    n = int(input())
    p = ceil(n/2)
    print('Q',p,0)
    sys.stdout.flush()
    a = int(input())
    print('Q',0,p)
    sys.stdout.flush()
    b = int(input())
    if(b<a):
        x = b
        y = n-b
    else:
        x = n-a
        y = a
    print('Q',10**9,y)
    sys.stdout.flush()
    m = int(input())
    m = 10**9-m
    print('Q',x,10**9)
    sys.stdout.flush()
    n = int(input())
    n = 10**9-n
    print('A',x,y,m,n)
