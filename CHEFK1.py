from math import ceil
for i in range(int(input())):
    n,k = [int(j) for j in input().split()]
    if(k<n-1 or k>(n*(n+1))//2):
        print(-1)
    elif(n==1 and k==0):
        print(0)
    elif(k==1):
        print(1)        
    elif(k<=n+1):
        print(2)
    elif(k<=2*n):
        print(3)
    else:
        print(ceil((k-n-n)*2/n)+3)
        
