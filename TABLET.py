for i in range(int(input())):
    n,b = [int(j) for j in input().split()]
    m = -1
    for j in range(n):
        w,h,p = [int(k) for k in input().split()]
        if(w*h>m and p<=b):
            m = int(w*h)
    if(m>-1):
        print(m)
    else:
        print('no tablet')
