def fun(a,b):
    l = b-a+1
    s = []
    if(l>6):
        for i in range(a,b+1):
           print(1,a,(a+1 if a+1<=b else a+1-b),(a+2 if a+2<=b else a+2-b))
           s.append(int(input()))
    else:
        for i in range(a,b+1):
           print(1,a,(a+1 if a+1<=b else a+1-b),(a+3 if a+3<=b else a+3-b))
           s.append(int(input()))

        for i in range(len(s)):
            

for i in range(int(input())):
    n = int(input())
    s = []
    for j in range(1,n+1,4):
        if(j+6<n):
            s.extend(fun(j,j+3))
        elif(j+3<n+1):
            s.extend(fun(j,n))
    print(2,*s)
