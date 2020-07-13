for i in range(int(input())):
    n = int(input())
    a = [int(j) for j in input().split()]
    p,i,c = a[0],1,0
    while(i<n):
        i+=p
        p+=sum(a[i-p:i])
        c+=1
    print(c)
