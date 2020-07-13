import sys
n,c = [int(i) for i in input().split()]
s,l,r = 1,0,n
m = 0
a = 0
p = 1
while(l<r):
    m = l+1
    cnt = 1
    if(m>=r):
        break
    while(m<r):
        print('1 '+str(m))
        sys.stdout.flush()
        s = int(input())
        if(s):
            r = m
            print(2)
        else:
           a = m
           m = a+cnt
           cnt = cnt<<1
    l = a
print('3 '+str(m))
