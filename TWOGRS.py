for i in range(int(input())):
    a,b,c = [int(j) for j in input().split()]
    f = 0
    if(c%2!=0):
        if((a%2!=0 and b%2!=0) or (a>2 and a%2!=0)):
            f=1
        elif(b>1 and a%2!=0 and b%2==0):
            f=1
    elif(b%2!=0):
        if((b>2 and a%2==0 and c>1) or (a>1 and a%2==0)):
            f=1
        elif(a%2==0):
            f=1
    if(f==1):
        print('YES')
    else:
        print('NO')
