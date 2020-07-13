for i in range(int(input())):
    n = int(input())
    n-=1
    a,b,c = 0,0,0
    p = n%26
    q = 2**int(n/26)
    if(p==0 or p==1):
        a = q
    elif(p>1 and p<10):
        b = q
    else:
        c = q
    print(a,b,c)
