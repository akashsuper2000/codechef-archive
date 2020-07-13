for i in range(int(input())):
    n = int(input())
    if(n==1):
        print(1)
        print(1,1)
        continue
    print(n//2)
    if(n==2):
        print(2,1,2)
        continue
    if(n%2==0):
        for j in range(1,n//2+1):
            print(2,j*2-1,j*2)
    else:
        print(3,1,2,3)
        for j in range(2,n//2+1):
            print(2,j*2,j*2+1)
