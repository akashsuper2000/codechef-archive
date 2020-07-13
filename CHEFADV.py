for i in range(int(input())):
    n,m,x,y = [int(j) for j in input().split()]
    if((n-1)%x==0 and (m-1)%y==0):
        print('Chefirnemo')
    elif(n-2>=0 and m-2>=0):
        if((n-2)%x==0 and (m-2)%y==0):
            print('Chefirnemo')
        else:
            print('Pofik')
    else:
        print('Pofik')
