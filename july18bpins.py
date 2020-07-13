for i in range(int(input())):
    a=int(input())
    if a==1:
        print(str(1)+' '+str(1))
    else:
        b=int(str(1)+str(0)*(a%2)+(a//2)*str(9))-2*
        print(str(b)+' '+str(10**a))
