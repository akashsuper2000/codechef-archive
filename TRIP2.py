for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    a = [int(j) for j in input().split()]
    if(n==1):
        if(a[0]==-1):
            a[0]=1
        print('YES')
        print(a[0])
    elif(n==2):
        if(a[0]==-1):
            if(a[1]==1):
                a[0]=2
            else:
                a[0]=1
        if(a[1]==-1):
            a[1]=2
        print('YES')
        print(*a)
    else:
        f = 1
        c = 0
        if(a.count(-1)!=n):
            if(a[0]==-1):
                j=0
                while(a[j]==-1):
                    j+=1
                j-=1
                while(j>=0):
                    if(a[j+1]==1):
                        a[j]=2
                    else:
                        a[j]=1
                    j-=1
            if(a[-1]==-1):
                j=n-1
                while(a[j]==-1):
                    j-=1
                j+=1
                while(j<n):
                    if(a[j-1]==1):
                        a[j]=2
                    else:
                        a[j]=1
                    j+=1
        else:
            a[0]=1
        c = a[0]
        for j in range(1,n-1):
            if(a[j]!=-1):
                c = a[j]
            else:
                if(a[j-1]!=1 and a[j+1]!=1):
                    a[j]=1
                elif(a[j-1]!=2 and a[j+1]!=2):
                    a[j]=2
                elif(k>2):
                    a[j]=3
                else:
                    f=0
                    break
                c = a[j]
        if(a[-1]==-1):
            if(a[-2]==1):
                a[-1]=2
            else:
                a[-1]=1
        for j in range(1,n):
            if(a[j-1]==a[j]):
                f = 0
                break
        if(f==0):
            print('NO')
        else:
            print('YES')
            print(*a)
                
