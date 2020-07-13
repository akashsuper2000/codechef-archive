def fun(a,b,c):
    if(c>b-a+1):
        return 0
    return ((b-a+1)//c) + fun(a,b,c*2)

for i in range(int(input())):
    a,b = [int(j) for j in input().split()]
    c = b*(b+1)//2 - a*(a-1)//2
    c-=fun()
    
