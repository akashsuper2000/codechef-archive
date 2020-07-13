for i in range(int(input())):
    a=[]
    f = 1
    for j in range(int(input())):
        x,y,l = [int(k) for k in input().split()]
        a.append([x,y,l])
    for i in range(len(a)-1):
        c = 0
        for j in range(i+1,len(a)):
            if(a[i][2]==a[j][2]):
                if(a[i][0]<=a[j][0]<=a[i][1] or a[i][0]<=a[j][1]<=a[i][1]):
                    c+=1
        if(c>1):
            f = 0
            break
    
    if(f==1):
        print('YES')
    else:
        print('NO')
