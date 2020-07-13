for i in range(int(input())):
    n = int(input())
    f,i = 1,0
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    while(i+2<n):
        if(a[i]>b[i]):
            f = 0
            break
        elif(b[i]>0):
            p = b[i]-a[i]
            b[i]-=p
            b[i+1]-=int(2*p)
            b[i+2]-=int(3*p)
            if(b[i+1]<a[i+1] or b[i+2]<a[i+2]):
                f = 0
                break
        i+=1
    if(b[-2]!=a[-2] or b[-1]!=a[-1]):
        f = 0
    if(f==1):
        print('TAK')
    else:
        print('NIE')
            
