import sys
l = 10**9
for i in range(int(input())):
    print('Q',0,0)
    sys.stdout.flush()
    p = int(input())
    print('Q',l,0)
    sys.stdout.flush()
    q = int(input())
    print('Q',0,l)
    sys.stdout.flush()
    s = int(input())
    print('Q',l,l)
    sys.stdout.flush()
    r = int(input())
    print('Q',int((s-r+l)/2),0)
    sys.stdout.flush()
    b = int(input())
    a = p-b
    x = b-q+l
    y = a-s+l
    print('A',a,b,x,y)
    sys.stdout.flush()
    a = int(input())
        
